import cv2
from Capture import Capture
from PyQt4 import QtGui, QtCore


class Window(QtGui.QWidget):
    def __init__(self):

        QtGui.QWidget.__init__(self)
        self.setWindowTitle('Control Panel')

        self.capture = Capture()
        self.start_button = QtGui.QPushButton('Begin Session',self)
        self.start_button.clicked.connect(self.capture.startCapture)

        self.end_button = QtGui.QPushButton('End Session',self)
        self.end_button.clicked.connect(self.capture.endCapture)

        self.login_button = QtGui.QPushButton('Login',self)
        # self.login_button.clicked.connect(self.capture.startCapture)


        # self.end_button = QtGui.QPushButton('End Session',self)
        # self.end_button.clicked.connect(self.capture.endCapture)

        self.quit_button = QtGui.QPushButton('Quit',self)
        self.quit_button.clicked.connect(self.capture.quitCapture)

        vbox = QtGui.QVBoxLayout(self)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.end_button)
        vbox.addWidget(self.login_button)
        vbox.addWidget(self.quit_button)

        self.setLayout(vbox)
        self.setGeometry(200,200,300,300)
        self.show()

    def mousePressEvent(self, QMouseEvent):
        print QMouseEvent.pos()

    def mouseReleaseEvent(self, QMouseEvent):
        cursor =QtGui.QCursor()
        print cursor.pos()
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
