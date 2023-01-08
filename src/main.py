from Board import Board


def determine_next_state(cell):
    alive_neighbors = sum(neighbor.state for neighbor in cell.neighbors)

    # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    if cell.state == 0:
        if alive_neighbors == 3:
            return 1
    # Any live cell with two or three live neighbors lives on to the next generation.
    elif cell.state == 1 and alive_neighbors in [2, 3]:
        return 1
    # Any live cell with fewer than two live neighbors dies, as if by underpopulation.
    elif cell.state == 1 and alive_neighbors < 2:
        return 0
    # Any live cell with more than three live neighbors dies, as if by overpopulation.
    elif cell.state == 1 and alive_neighbors > 3:
        return 0


if __name__ == "__main__":
    board = Board([[1, 1], [1, 0]])
    for row in board.board:
        for cell in row:
            print(f"Current state: {cell.state}, Neighbours: {cell.neighbors} Next state: {determine_next_state(cell)}")
