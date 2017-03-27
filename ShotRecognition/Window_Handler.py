class WindowState:
    LOADING_SCREEN = 0
    LOGIN_SCREEN = 1
    MENU_SCREEN = 2
    CAPTURE_SCREEN = 3

class Window_Handler:

    def __init__(self, initial_state):
        self.state_stack = []
        self.state_stack.push(initial_state)

        self.available_states = []

    def current_state(self):
        return self.state_stack.peek()

    # Enter a new state
    def go_to_state(self, state):
        if self.current_state() == state:
            return -1
        if self.current_state() in self.available_states:
            return state


    # Go back one state
    def go_back(self):
        self.state_stack.pop()
        return
