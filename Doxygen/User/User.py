class User:
    """
    This class creates a user object. It is used to keep track of all logged in users.
    """
    def __init__(self):
        """
        This initializes the userID and username of the user.
        """
        self.userId = None
        self.username = None

    def login(self,uID):
        """This logs in a user once their ID is verified."""
        if (self.userId == None):
            self.userId = uID
            return self.userId
        return -1

    def logout(self,uID):
        """Removes the logged out user."""
        if (self.userId == uID):
            self.userId = None
            return self.userId
        return -1

    def getCurrentUser(self):
        """Returns the current logged in user."""
        return self.userId

    def isLoggedIn(self):
        """Returns True if the user is logged in.
           Returns false otherwise.
        """
        if (self.userId == None):
            return False
        return True
