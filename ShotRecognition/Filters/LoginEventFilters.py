from PyQt4 import QtCore

class UsernameEventFilter(QtCore.QObject):

    def eventFilter(self, widget, event):
        # FocusOut event
        if event.type() == QtCore.QEvent.FocusIn:
            if widget.text() == "Username":
                widget.setText("")
        elif event.type() == QtCore.QEvent.FocusOut:
            if widget.text() == "":
                widget.setText("Username")
        return False

class PasswordEventFilter(QtCore.QObject):

    def eventFilter(self, widget, event):
        # FocusOut event
        if event.type() == QtCore.QEvent.FocusIn:
            if widget.text() == "Password":
                widget.setText("")
        elif event.type() == QtCore.QEvent.FocusOut:
            if widget.text() == "":
                widget.setText("Password")
        return False
