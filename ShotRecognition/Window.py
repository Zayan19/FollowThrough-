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
import User


class Window(QtGui.QMainWindow):
    window_state = 0;

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.setWindowTitle('FollowThrough')

        wid = QtGui.QWidget(self)
        self.setCentralWidget(wid)
        # p = wid.palette()
        # p.setColor(wid.backgroundRole(), QtGui.QColor.red)
        # wid.setPalette(p)
        wid.setStyleSheet("background-color:white;")

        main_layout = QtGui.QGridLayout()

        self.label = QtGui.QLabel()
        self.pixmap = QtGui.QPixmap('resources/followthrough_logo.png')
        self.label.setPixmap(self.pixmap)

        self.login_button = QtGui.QPushButton('Login')
        self.login_button.clicked.connect(self.click_login)

        self.logout_button = QtGui.QPushButton('Logout')
        self.logout_button.clicked.connect(self.click_login)

        main_layout.addWidget(self.label,0,1)
        main_layout.addWidget(self.login_button,1,1)
        main_layout.addWidget(self.logout_button,2,1)


        wid.setLayout(main_layout)
        self.setGeometry(200,200,500,500)
        self.show()

    def click_login(self):
        login = Login(self)
        if login.exec_():   # here dialog will be shown and main script will wait for its closing (with no errors)
            data = login.textName.text()
            print data
            # if (data ['userId'] != -1):
            #     User.setId(data['userId'])

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
