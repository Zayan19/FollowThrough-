from PyQt4 import QtGui
from Networking import Login_Handler
from Filters.LoginEventFilters import UsernameEventFilter, PasswordEventFilter


class LoginWindow(QtGui.QDialog):
    """
    This class handles the login window. This is the window that appears
    when the user first opens the application. This is needed because all the data
    the program processes should be uploaded to the user's account.
    """

    style ='''
    QLabel
    {
        font-family: Times New Roman;
        font-size: 18pt;
    }
    '''

    # constructor
    def __init__(self, parent=None):

        """
        This is an intializer used to  intialize the fields that are required for the login screen
        In particular it initializes:

               1.Login filter
               2.Password Filter
               3.Username Area
               4.Password Area
               5.Login Button

        """



        super(LoginWindow, self).__init__(parent)

        ''' Define all gui elements '''
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
        """Handles Login submission by posting to server.
        Confirms the user has entered a username
        It attempts to login to the server.
        If user ID is found, user is logged in.
        Otherwise displays warning message."""



        if (len(self.textName.text()) >= 0 and self.textName.text() != "Username"):
            ''' Confirm that the user has entered a username '''
            login_handler = Login_Handler(self.textName.text(),self.textPass.text())
            self.data = login_handler.post('http://54.145.183.186/api/user')

            ''' Check if the user was properly logged in. '''
            if self.data['userId'] == -1:
                QtGui.QMessageBox.warning(self, 'Error', 'Login failed, please try again!')
            else:
                self.accept()
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'Please enter your username and password!')
