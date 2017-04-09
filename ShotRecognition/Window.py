"""@package ShotRecognition
    This module creates and handles all gui windows and drawing to them.
"""
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
# from Capture import Capture
from Ball_Tracker import Ball_Tracker
from PyQt4 import QtGui, QtCore
from State import State
from Login import LoginWindow
from PositionSelector import PositionSelectorWindow
from User import User



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

        self.user = User()

        self.setWindowTitle('FollowThrough')

        wid = QtGui.QWidget(self)
        self.setCentralWidget(wid)

        wid.setStyleSheet("background-color:white;")

        main_layout = QtGui.QGridLayout()

        label = QtGui.QLabel()
        self.pixmap = QtGui.QPixmap('resources/followthrough_logo.png')
        label.setPixmap(self.pixmap)


        self.login_button = QtGui.QPushButton('Login')
        self.login_button.clicked.connect(self.click_login)

        self.select_position = QtGui.QPushButton('Select Position')
        self.select_position.clicked.connect(self.click_select_position)

        self.capture_video = QtGui.QPushButton('Capture Video')
        self.capture_video.clicked.connect(self.click_capture_video)

        self.load_video = QtGui.QPushButton('Load Video from File')
        self.load_video.clicked.connect(self.click_load_video)

        self.logout_button = QtGui.QPushButton('Logout')
        self.logout_button.clicked.connect(self.click_logout)

        self.buttons = [self.login_button, self.select_position, self.capture_video, self.logout_button,self.load_video]

        self.user.login('5')

        self.update_button_state()

        for item in self.buttons:
            item.setStyleSheet(self.button_style)

        main_layout.addWidget(label,0,1)
        main_layout.addWidget(self.login_button,1,1)
        main_layout.addWidget(self.select_position,3,1)
        main_layout.addWidget(self.capture_video,2,1)
        main_layout.addWidget(self.load_video,4,1)
        main_layout.addWidget(self.logout_button,5,1)

        wid.setLayout(main_layout)

        # self.setGeometry(200,200,600,500)
        self.setFixedSize(self.size())
        self.show()

    def click_login(self):
        login = LoginWindow(self)
        if login.exec_():   # here dialog will be shown and main script will wait for its closing (with no errors)
            self.user.login(login.data['userId'])
            self.update_button_state()

        else:
            print ("error closing")

    def click_select_position(self):
        position_selector = PositionSelectorWindow(self)
        if position_selector.exec_():   # here dialog will be shown and main script will wait for its closing (with no errors)
            # self.user.login(login.data['userId'])
            # self.update_button_state()
            pass
        else:
            print ("error closing")

    def click_capture_video(self):
        pass
    def click_load_video(self):
        filename = QtGui.QFileDialog.getOpenFileName()
        print filename
        if filename:
            Ball_Tracker('Ball Tracker', cv2.VideoCapture(str(filename))).run()


    def click_logout(self):
        self.user.logout(self.user.getCurrentUser())
        self.update_button_state()

    def update_button_state(self):
        if (self.user.isLoggedIn()):
            self.login_button.setEnabled(False)
            self.select_position.setEnabled(True)
            self.capture_video.setEnabled(True)
            self.logout_button.setEnabled(True)
            self.load_video.setEnabled(True)
        else:
            self.login_button.setEnabled(True)

            self.select_position.setEnabled(False)
            self.capture_video.setEnabled(False)
            self.logout_button.setEnabled(False)
            self.load_video.setEnabled(False)

    # def mousePressEvent(self, QMouseEvent):
    #     print QMouseEvent.pos()
    #
    # def mouseReleaseEvent(self, QMouseEvent):
    #     cursor =QtGui.QCursor()
    #     print cursor.pos()


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    #
    # if login.exec_() == QtGui.QDialog.Accepted:
    #     window = Window()
    #     window.show()
    sys.exit(app.exec_())
