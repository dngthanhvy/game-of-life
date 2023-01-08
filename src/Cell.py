class Cell:
    def __init__(self, state, neighbors=[]):
        self.state = state
        self.neighbors = neighbors
        self.next_state = None

    def set_next_state(self):
        alive_neighbors = sum(neighbor.state for neighbor in self.neighbors)

        # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        if self.state == 0:
            if alive_neighbors == 3:
                self.next_state = 1
            self.next_state = 0
        # Any live cell with two or three live neighbors lives on to the next generation.
        elif self.state == 1 and alive_neighbors in [2, 3]:
            self.next_state = 1
        # Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        elif self.state == 1 and alive_neighbors < 2:
            self.next_state = 0
        # Any live cell with more than three live neighbors dies, as if by overpopulation.
        elif self.state == 1 and alive_neighbors > 3:
            self.next_state = 0

    def update(self):
        self.state = self.next_state
        self.next_state = None

    def __str__(self):
        return str(self.state)

    def __repr__(self):
        return str(self.state)
