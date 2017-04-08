from PyQt4 import QtGui
# from Networking import Login_Handler
# from Filters.LoginEventFilters import UsernameEventFilter, PasswordEventFilter
#
# class PositionSelector:
#     def __init__(self):
#         self.capturing = False
#         self.c = cv2.VideoCapture(0)
#
#     def startCapture(self):
#         print "pressed start"
#         self.capturing = True
#         cap = self.c
#         while(self.capturing):
#             ret, frame = cap.read()
#             cv2.imshow("Capture", frame)
#             cv2.waitKey(5)
#         cv2.destroyAllWindows()
#
#     def endCapture(self):
#         print "pressed End"
#         self.capturing = False
#
#     def quitCapture(self):
#         print "pressed Quit"
#         cap = self.c
#         cv2.destroyAllWindows()
#         cap.release()
#         QtCore.QCoreApplication.quit()



from PyQt4 import QtGui
from Networking import Login_Handler
from Filters.LoginEventFilters import UsernameEventFilter, PasswordEventFilter


# TODO: Doxygen
class LoginWindow(QtGui.QDialog):

    style ='''
    QLabel
    {
        font-family: Times New Roman;
        font-size: 18pt;
    }
    '''

    # TODO: Doxygen
    # constructor
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)

        # Define filters
        self.login_filter = UsernameEventFilter()
        self.password_filter = PasswordEventFilter()

        # Login login_label
        self.title_label = QtGui.QLabel("Choose Position")
        self.title_label.setStyleSheet(self.style)


        # login button
        # self.buttonLogin = QtGui.QPushButton('Login', self)
        # self.buttonLogin.clicked.connect(self.handleLogin)

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.title_label)


    # TODO: Doxygen
    # handles loging submission
    # def handleLogin(self):
    #     if (len(self.textName.text()) >= 0 and self.textName.text() != "Username"):
    #         # Attempt to login with the server
    #         login_handler = Login_Handler(self.textName.text(),self.textPass.text())
    #         self.data = login_handler.post('http://54.145.183.186/api/user')
    #
    #         if self.data['userId'] == -1:
    #             QtGui.QMessageBox.warning(self, 'Error', 'Login failed, please try again!')
    #         else:
    #             print self.data
    #             self.accept()
    #     else:
    #         QtGui.QMessageBox.warning(self, 'Error', 'Please enter your username and password!')
