from PyQt4 import QtGui
from Networking import Login_Handler
from Filters.LoginEventFilters import UsernameEventFilter, PasswordEventFilter


# TODO: Doxygen
class PositionSelectorWindow(QtGui.QDialog):

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
        super(PositionSelectorWindow, self).__init__(parent)
        # self.click_handler = ClickHandler()

        # Define filters
        self.login_filter = UsernameEventFilter()
        self.password_filter = PasswordEventFilter()

        # Login login_label
        self.title_label = QtGui.QLabel("Choose Position")
        self.title_label.setStyleSheet(self.style)
        # main_layout = QtGui.QGridLayout()

        self.label = QtGui.QLabel()
        self.pixmap = QtGui.QPixmap('resources/basketball_halfcourt.gif')
        self.label.setPixmap(self.pixmap)

        # login button
        # self.buttonLogin = QtGui.QPushButton('Login', self)
        # self.buttonLogin.clicked.connect(self.handleLogin)


        layout = QtGui.QGridLayout(self)

        layout.addWidget(self.title_label,0,0)
        layout.addWidget(self.label,0,0)
    def mousePressEvent(self, QMouseEvent):
        cursor = QtGui.QCursor()

        print QMouseEvent.pos()

    def mouseReleaseEvent(self, QMouseEvent):
        cursor = QtGui.QCursor()
        print cursor.pos()
