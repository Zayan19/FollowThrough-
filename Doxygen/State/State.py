
from PyQt4 import QtGui, QtCore

class State:
    """
    This helper class is used to handle the state of the GUI application
    that is designed for the user. The application is designed using QtGui
    which is an open source graphics module. It was chosen for its robustness.
    """
    def __init__(self, state=0, layout="vbox"):
        """

        Constructor used to initialize the layout objecti.
        Initially the widget list is empty as the number of widgets are 0.
        """
        self.state = state
        self.widgets = []
        self.num_of_widgets = 0
        # Create the layout object
        if layout == "vbox":
            self.layout = QtGui.QVBoxLayout()
        elif layout == "grid":
            self.layout = QtGui.QGridLayout()

    def get_layout (self):
        """Return the layout"""
        return self.layout

    def add_widget(self, widget, position="None"):
        "Add a new given widget on the window"

        if type(position) is tuple:
            self.layout.addWidget(widget, *position)
        else:
            self.layout.addWidget(widget)

        self.widgets.append(widget)

    def remove_all_widgets(self):
        """Method to remove all widgets"""
        for i in self.widgets:
            self.layout.remove_widget()
        self.widgets = []

    def remove_widget(self, widget):
        """Method to remove a given widget"""
        self.layout.removeWidget(widget)

    def get_widgets(self):
        """Method to return current widgets"""
        return self.widgets
