from Cell import Cell


def _transform_board(raw_board):
    board = [[Cell(cell) for cell in row] for row in raw_board]
    for row in range(len(board)):
        for col in range(len(board[0])):
            cell = board[row][col]
            cell.neighbors = _get_neighbours(board, row, col)
    return board


def _get_neighbours(board, row, col):
    left = board[row][max(col - 1, 0)]
    right = board[row][min(col + 1, len(board[0]) - 1)]
    top = board[max(row - 1, 0)][col]
    bottom = board[min(row + 1, len(board) - 1)][col]
    return [neighbor for neighbor in [left, right, top, bottom] if
            neighbor is not None and neighbor is not board[row][col]]


class Board:
    def __init__(self, board):
        self.board = _transform_board(board)
