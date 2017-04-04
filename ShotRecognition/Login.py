from PyQt4 import QtGui
from Networking import Login_Handler
from Filters.LoginEventFilters import UsernameEventFilter, PasswordEventFilter


# TODO: Doxygen
class Login(QtGui.QDialog):

    style ='''
    QLabel
    {
        font-family: Times New Roman;
        font-size: 18pt;
    }
    '''

    # TODO: Doxygen
    # constructor
    def __init__(self, dbConnection, parent=None):
        super(Login, self).__init__(parent)


        # Define filters
        self.login_filter = UsernameEventFilter()
        self.password_filter = PasswordEventFilter()

        # Login login_label
        self.login_label = QtGui.QLabel("Login")
        self.login_label.setStyleSheet(self.style)

        # Username Area
        self.textName = QtGui.QLineEdit("Username",self)
        self.textName.installEventFilter(self.login_filter)

        # Password area
        self.textPass = QtGui.QLineEdit("Password", self)
        self.textPass.installEventFilter(self.password_filter)
        self.textPass.setEchoMode(QtGui.QLineEdit.Password)

        # login button
        self.buttonLogin = QtGui.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)



        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.login_label)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    # TODO: Doxygen
    # handles loging submission
    def handleLogin(self):

        if ():
            self.accept()
        else:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Bad user or password')
