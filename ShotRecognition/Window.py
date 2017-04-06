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
    button_style = '''
                QPushButton {
                    border: 1px solid grey;
                    width:100%;
                    margin-left: 150px;
                    margin-right: 150px;
                    margin-bottom: 3px;
                    padding-top: 3px;
                    padding-bottom:3px;
                }
                QPushButton:pressed {
                    border: 1px solid grey;
                    width:100%;
                    margin-left: 150px;
                    margin-right: 150px;
                    margin-bottom: 3px;
                    padding-top: 3px;
                    padding-bottom:3px;
                    background-color:grey;
                }

                '''
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

        label = QtGui.QLabel()
        self.pixmap = QtGui.QPixmap('resources/followthrough_logo.png')
        label.setPixmap(self.pixmap)
        # label.setStyleSheet()

        login_button = QtGui.QPushButton('Login')
        login_button.clicked.connect(self.click_login)

        select_position = QtGui.QPushButton('Select Position')
        # self.select_position.clicked.connect(self.select_position)

        capture_video = QtGui.QPushButton('Capture Video')
        # self.capture_video.clicked.connect(self.begin_capture)


        logout_button = QtGui.QPushButton('Logout')
        logout_button.clicked.connect(self.click_login)

        self.buttons = [login_button, select_position, capture_video, logout_button]

        for item in self.buttons:
            item.setStyleSheet(self.button_style)

        main_layout.addWidget(label,0,1)
        main_layout.addWidget(login_button,1,1)
        main_layout.addWidget(select_position,3,1)
        main_layout.addWidget(capture_video,2,1)
        main_layout.addWidget(logout_button,4,1)



        wid.setLayout(main_layout)
        # self.setGeometry(200,200,600,500)
        self.setFixedSize(self.size())
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
