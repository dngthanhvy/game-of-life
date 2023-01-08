class Cell:
    def __init__(self, state, neighbors=[]):
        self.state = state
        self.neighbors = neighbors
        self.last_state = None

    def update(self, next_state):
        self.last_state = self.state
        self.state = next_state

    def __str__(self):
        return str(self.state)

    def __repr__(self):
        return str(self.state)
