import cv2
from managers import WindowManager, CaptureManager

class Ball_Tracker(object):

    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)

        self._bs = cv2.createBackgroundSubtractorKNN(detectShadows = True)

    def run(self):
        """Run the main loop"""
        self._windowManager.createWindow()

        while self._windowManager.isWindowCreated: 
            self._captureManager.enterFrame()
            frame = self._captureManager.frame

            # TODO: Filter the frame
            fgmask = self._bs.apply(frame)
            th = cv2.threshold(fgmask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
            erroded = cv2.erode(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3)), iterations = 2)
            dilated = cv2.dilate(erroded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3)), iterations = 2)

            self._captureManager.frame = dilated


            self._captureManager.exitFrame()
            self._windowManager.processEvents()


    def onKeypress(self, keycode):
        """
            Handle a keypress
            
            space -> Take a screenshot
            tab -> start / stop recording a screencast
            esc -> quit
        """

            # spacebar
        if keycode == 32: 
            self._captureManager.writeImage('screenshot.png')
            # tab
        elif keycode == 9:
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
            # esc
        elif keycode == 27:
            self._windowManager.destroyWindow()
    
if __name__ == '__main__':
   Ball_Tracker().run()

