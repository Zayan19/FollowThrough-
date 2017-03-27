class WindowState:
    LOADING_SCREEN = 0
    LOGIN_SCREEN = 1
    MENU_SCREEN = 2
    CAPTURE_SCREEN = 3
    
class Window_Handler:

    def __init__(self):
        self.state_stack = []


    def current_state(self):
        pass
    # Enter a new state
    def go_to_state(self, state):
        # If we are going to a new state push it on the stack
        if self.state_stack[len(self.state_stack)-1] != state:
            self.state_stack.push(state)
        return

    # Go back one state
    def go_back(self):
        self.state_stack.pop()
