"""@package ShotRecognition
    This module creates and handles all gui windows and drawing to them.
"""
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
from Capture import Capture
from Ball_Tracker import Ball_Tracker
from PyQt4 import QtGui, QtCore
from State import State
from Login import Login
class Window(QtGui.QMainWindow):
    window_state = 0;

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setWindowTitle('FollowThrough')

        # state = self.init_login_state()


        # if login.exec_() == QtGui.QDialog.Accepted:
        #     window = Window()
        #     window.show()
        #     sys.exit(app.exec_())

        # self.bal_tracker = Ball_Tracker(True, None)

        # self.capture = Capture()
        # if (self.menu):
        #     self.start_button = QtGui.QPushButton('Begin Session')
        #     self.start_button.clicked.connect(self.capture.startCapture)

        # self.end_button = QtGui.QPushButton('End Session')
        # # self.end_button.clicked.connect(self.capture.endCapture)
        #
        self.login_button = QtGui.QPushButton('Login', self)
        # self.login_button.clicked.connect(self.login)
        self.login_button.clicked.connect(self.showDial)

        # self.setLayout(state.get_layout())
        self.setGeometry(200,200,500,500)
        self.show()

    def showDial(self):
        login = Login("",self)
        if login.exec_():   # here dialog will be shown and main script will wait for its closing (with no errors)
            data = dialog.line_edit.text()

    #state ID = 0
    def init_login_state(self):
        state = State(1, "grid")

        return state
    #state ID=1
    def init_login_state(self):
        state = State(1, "grid")

        # username = QtGui.QTextEdit(self)
        # password = QtGui.QTextEdit(self)
        # login_button = QtGui.QPushButton('Login')
        #
        #
        # inner_lay = QtGui.QVBoxLayout()
        # inner_lay.addWidget(username)
        # inner_lay.addWidget(password)
        # inner_lay.addWidget(login_button)
        # # state.layout.setColumnMinimumWidth(3)
        # # state.layout.setRowMinimumHeight(3)
        #
        # state.layout.setRowStretch(0,1)
        # state.layout.setColumnStretch(0,2)
        # state.layout.setColumnStretch(1,1)
        # state.layout.setColumnStretch(2,2)
        #
        # state.layout.addLayout(inner_lay, 0,1)
        #





        # state.add_widget(login_button, (1,4))

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
    #
    # if login.exec_() == QtGui.QDialog.Accepted:
    #     window = Window()
    #     window.show()
    sys.exit(app.exec_())
