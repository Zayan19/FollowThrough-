from PyQt4 import QtGui, QtCore

from Networking import Login_Handler



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
        # self.login_filter = UsernameEventFilter()
        # self.password_filter = PasswordEventFilter()

        # Login login_label
        # self.title_label = QtGui.QLabel("Choose Position")
        # self.title_label.setStyleSheet(self.style)
        # main_layout = QtGui.QGridLayout()

        self.bball_label = BasketballLabel(self,QtCore.QPoint(100,330), 30)


        # login button
        # self.buttonLogin = QtGui.QPushButton('Login', self)
        # self.buttonLogin.clicked.connect(self.handleLogin)


        layout = QtGui.QGridLayout(self)
        # self.label.lower()

        # layout.addWidget(self.title_label,0,0)
        layout.addWidget(self.bball_label,0,0)


class BasketballLabel(QtGui.QLabel):

    def __init__(self, parent=None, startingPosition=QtCore.QPoint(100,100), radius= 30):
        super(BasketballLabel, self).__init__(parent)
        self.playerPosition = startingPosition
        self.radius = radius


        self.mousePressEvent = self.mousePress
        self.image = QtGui.QImage('resources/basketball_halfcourt.gif')



    def paintEvent(self,event):
        painter=QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.drawImage(0, 0, self.image)
        painter.setPen(QtGui.QPen(QtCore.Qt.red,3))
        painter.drawEllipse(self.playerPosition.x() - self.radius/2,self.playerPosition.y() - self.radius/2, self.radius,self.radius)
        self.setPixmap(QtGui.QPixmap('resources/basketball_halfcourt.gif'))

        painter.end()


    def mousePress(self, event):
        self.playerPosition = event.pos()
        self.update()
        print event.pos()
