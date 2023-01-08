from Board import Board

if __name__ == "__main__":
    board = Board([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])

    print("Initial board:")
    print(board.board)

    for row in range(len(board.board)):
        for col in range(len(board.board[0])):
            board.board[row][col].set_next_state()

    print("Next board:")
    board.set_next()
    print(board.board)
