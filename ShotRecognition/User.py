class User:
    def __init__(self):
        self.userId = None
        self.username = None

    # Log in a user once their ID is verified
    def login(self,uID):
        if (self.userId == None):
            self.userId = uID
            return self.userId
        return -1

    # Remove the logged out user
    def logout(self,uID):
        if (self.userId == uID):
            self.userId = None
            return self.userId
        return -1

    # Returns the current logged in user
    def getCurrentUser(self):
        return self.userId

    def isLoggedIn(self):
        if (self.userId == None):
            return False
        return True
