
__userId = None
__username = None

# Log in a user once their ID is verified
def login(uID):
    if (__userId == None):
        __userId = uID
        return __userId
    return -1
    
# Remove the logged out user
def logout(uID):
    if (__userId == uID):
        __userId = None
        return __userId
    return -1

# Returns the current logged in user
def getCurrentUser():
    return __userId

def isLoggedIn():
    if (__userId == None):
        return False
    return True
