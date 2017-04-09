import cv2
import numpy
from time import time

class CaptureManager(object):
    """
    The CaptureManager class handles the capturing and processing of the image and video files
    using openCV. It gives the ability to take screenshots and/or record a video while the application is running.
    """
    def __init__(self, capture, previewWindowManager = None, shouldMirrorPreview = False):

        """
        Constructor used to initialize class variables/functions:

        1. previewWindowManager -The current window being managed that displays the application.
        2. capture              -Captured video/image
        3. channel              -Initial colour channel
        4. _enteredFrame        -Boolean used to check if a new frame has been entered
        5. _frame               -Current frame
        6. _imageFileName       -Name of image file
        7. _videoFileName       -Name of video file
        8. _videoEncoding       -Type of encoding used for video that gets recorded
        9. _videoWriter         -Used to record video if user wishes
        10 _startTime           -Starting time of video
        11._framesElapsed       -Number of frames that have elapsed since video began
        12._fpsEstimate         -How many frames per second the video is running


        """
        self.previewWindowManager = previewWindowManager
        self.shouldMirrorPreview = shouldMirrorPreview

        self._capture = capture
        self._channel = 0
        self._enteredFrame = False
        self._frame = None
        self._imageFileName = None
        self._videoFileName = None
        self._videoEncoding = None
        self._videoWriter = None

        self._startTime = None
        self._framesElapsed = 0
        self._fpsEstimate = None

    @property
    def channel(self):
        """Returns channel."""
        return self._channel

    @channel.setter
    def channel(self, value):
        """Sets channel."""
        if self._channel != value:
            self._channel = value
            self._frame = None

    @property
    def frame(self):
        """Retrieves the next frame if possible."""
        if self._enteredFrame and self._frame is None:
            _, self._frame = self._capture.retrieve()
        return self._frame

    @frame.setter
    def frame(self, frame):
        """Sets the next frame."""
        if self._frame != frame:
            self._frame = frame

    @property
    def isWritingImage(self):
        """Checks if image exists."""
        return self._imageFileName is not None

    @property
    def isWritingVideo(self):
        """Checks if video exists."""
        return self._videoFileName is not None


    def enterFrame(self):
        """Capture the next frame, if any."""

        # First, check that any previous frame was exited.
        assert not self._enteredFrame, "previous enterFrame() had no matching exitFrame()"

        if self._capture is not None:
            self._enteredFrame = self._capture.grab()

    def exitFrame(self):
        """
        Draw to the window. Write to files. Release the frame.
        This is done with the following steps:

        1.
        Check whether any grabbed frame is retrievable.
        The getter may retrieve and cache the frame.
        2.
        Update the FPS estimate and related variables.
        3.
        Draws to the window and writes to the image and video files if they exist
        """


        # Check whether any grabbed frame is retrievable
        # The getter may retrieve and cache the frame
        if self.frame is None:
            self._enteredFrame = False
            return

        # Update the FPS estimate and related vars
        if self._framesElapsed == 0:
            self._startTime = time()
        else:
            timeElapsed = time() - self._startTime
            self._fpsEstimate = self._framesElapsed / timeElapsed
        self._framesElapsed += 1

        # Draw to the window, if any
        if self.previewWindowManager is not None:
            if self.shouldMirrorPreview:
                mirroredFrame = numpy.fliplr(self._frame).copy()
                self.previewWindowManager.show(mirroredFrame)
            else:
                self.previewWindowManager.show(self._frame)

        # Write to the image file, if any
        if self.isWritingImage:
            cv2.imwrite(self._imageFileName, self._frame)
            self._imageFileName = None

        # Write to the video file, if any
        self._writeVideoFrame()

        # Release the frame
        self._frame = None
        self._enteredFrame = False


    def writeImage(self, filename):
        """Write the next exited frame to an image file"""
        self._imageFileName = filename
# v2.VideoWriter_fourcc('I', '4', '2', '0')):
    def startWritingVideo(self, filename,
            encoding = cv2.cv.CV_FOURCC(*'I420')):
        """Start writing exited frames to a video file"""
        self._videoFileName = filename
        self._videoEncoding = encoding

    def stopWritingVideo(self):
        """Stop writing exited frames to a video file"""
        self._videoFileName = None
        self._videoEncoding = None
        self._videoWriter = None

    def _writeVideoFrame(self):
        """
        Method used to write to video frame.

        """
        if not self.isWritingVideo:
            return

        if self._videoWriter is None:
            fps = self._capture.get(cv2.CAP_PROP_FPS)
            if fps == 0.0:
                # The capture's FPS is unknown so use the estimate
                if self._framesElapsed < 20:
                    # Wait until more frames elapse so the estimate is better
                    return
                else:
                    fps = self._fpsEstimate

            size = (int(self._capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                    int(self._capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            self._videoWriter = cv2.VideoWriter(self._videoFileName, self._videoEncoding, fps, size)

        self._videoWriter.write(self._frame)


class WindowManager(object):
    """
    Class used to handle the creation and properties of a window used to display the OpenCV application.

    """
    def __init__(self, windowName, keypressCallback = None):
        """
        Used to initialize windowname and keypressCallback variables.
        windowname = Application name
        keypressCallBack = Key used to handle events while application is running.

        """

        self.keypressCallback = keypressCallback

        self._windowName = windowName
        self._isWindowCreated = False

    @property
    def isWindowCreated(self):
        """Method is used to check if the window has been created yet.
           Returns true if window exists, false otherwise.        """
        return self._isWindowCreated

    def createWindow(self):
        """Method used to create window to display onscreen"""
        cv2.namedWindow(self._windowName)
        cv2.moveWindow(self._windowName, 0, 0)
        self._isWindowCreated = True

    def show(self, frame):
        """Method used to show active windows"""
        cv2.imshow(self._windowName, frame)

    def destroyWindow(self):
        """
         Method is used to destroy active windows.
        """
        cv2.destroyWindow(self._windowName)
        self._isWindowCreated = False

    def processEvents(self):
        """
        This method handles the events that may occur while the application is running and the video is being processed..
        In particular, it allows the user to pause and unpause the application with a keypress.

        """
        keycode = cv2.waitKey(1)
        if self.keypressCallback is not None and keycode != -1:
            # Discard any non-ASCII info encoded by GTK
            keycode &= 0xFF
            self.keypressCallback(keycode)
