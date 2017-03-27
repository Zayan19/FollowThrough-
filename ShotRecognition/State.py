from PyQt4 import QtGui, QtCore

class State:
    def __init__(self, state=0, layout="vbox"):
        self.state = state
        self.widgets = []
        self.num_of_widgets = 0
        # Create the layout object
        if layout == "vbox":
            self.layout = QtGui.QVBoxLayout()
        elif layout == "grid":
            self.layout = QtGui.QGridLayout()

    def get_layout (self):
        return self.layout

    def add_widget(self, widget):
        # add the widget to the layout and add it to the ist of widgets
        self.layout.addWidget(widget)
        self.widgets.append(widget)

    def remove_all_widgets(self):
        for i in self.widgets:
            self.layout.remove_widget()
        self.widgets = []

    def remove_widget(self, widget):
        self.layout.removeWidget(widget)

    def get_widgets(self):
        return self.widgets
