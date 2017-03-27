import cv2
from Capture import Capture
from Ball_Tracker import Ball_Tracker
from PyQt4 import QtGui, QtCore
from State import State

class Window(QtGui.QWidget):
    window_state = 0;

    def __init__(self):
        self.menu = False

        QtGui.QWidget.__init__(self)

        self.setWindowTitle('Control Panel')
        state = self.init_login_state()
        # self.bal_tracker = Ball_Tracker(True, None)

        # self.capture = Capture()
        # if (self.menu):
        #     self.start_button = QtGui.QPushButton('Begin Session')
        #     self.start_button.clicked.connect(self.capture.startCapture)

        # self.end_button = QtGui.QPushButton('End Session')
        # # self.end_button.clicked.connect(self.capture.endCapture)
        #
        # login_button = QtGui.QPushButton('Login')
        # # self.login_button.clicked.connect(self.capture.startCapture)
        #
        # quit_button = QtGui.QPushButton('Quit')
        # self.quit_button.clicked.connect(self.capture.quitCapture)

        # vbox = QtGui.QVBoxLayout(self)

        # vbox2 = QtGui.QVBoxLayout(self)

        # vbox.addWidget(self.start_button)
        # vbox.addWidget(self.end_button)
        # vbox.addWidget(self.login_button)
        # vbox2.addWidget(quit_button)

        self.setLayout(state.get_layout())
        self.setGeometry(200,200,900,900)
        self.show()

    #state ID=1
    def init_login_state(self):
        state = State(1, "grid")
        username = QtGui.QTextEdit(self)
        password = QtGui.QTextEdit(self)
        login_button = QtGui.QPushButton('Login')

        state.add_widget(username)
        state.add_widget(password)
        state.add_widget(login_button)
        return state

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
