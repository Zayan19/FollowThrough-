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

        self.bball_label = BasketballLabel(self,QtCore.QPoint(250,260), 10)

        # login button
        self.select_position = QtGui.QPushButton('Select Position', self)
        self.select_position.clicked.connect(self.click_select_position)


        layout = QtGui.QGridLayout(self)

        # layout.addWidget(self.title_label,0,0)
        layout.addWidget(self.bball_label,0,0)
        layout.addWidget(self.select_position,1,0)


    def click_select_position(self):
        self.zone = self.getZone()
        print (self.zone)
        # ret self.pos and self.zone
        self.accept()

    def getZone(self):

        x,y = self.bball_label.playerPosition.x(),self.bball_label.playerPosition.y()
        print (str(x) + " " + str(y))
        # zones 1,2,3
        if (y <= 275):
            if (x < 190):
                return 1
            elif(x<300):
                return 2
            else:
                return 3
        else:
            if (x < 190):
                return 4
            elif (x < 300):
                return 5
            else:
                return 6





class BasketballLabel(QtGui.QLabel):

    def __init__(self, parent=None, startingPosition=QtCore.QPoint(100,100), radius=10):
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
        painter.setPen(QtGui.QPen(QtCore.Qt.red,4))
        painter.drawEllipse(self.playerPosition.x() ,self.playerPosition.y(), self.radius,self.radius)

        painter.setPen(QtGui.QPen(QtCore.Qt.blue,2))
        painter.drawLine(306,0,306,500)
        painter.drawLine(193,0,193,500)
        painter.drawLine(0,273,600,273)

        painter.setPen(QtGui.QPen(QtCore.Qt.blue,2))

        painter.drawText(10,20,"1")
        painter.drawText(203,20,"2")
        painter.drawText(316,20,"3")

        painter.drawText(10,288,"4")
        painter.drawText(203,288,"5")
        painter.drawText(316,288,"6")


        self.setPixmap(QtGui.QPixmap('resources/basketball_halfcourt.gif'))
        painter.end()


    def mousePress(self, event):
        self.playerPosition = event.pos()
        self.playerPosition -= QtCore.QPoint(10,10)
        self.update()
        print event.pos()
