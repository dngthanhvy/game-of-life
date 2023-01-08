from Board import Board

if __name__ == "__main__":
    board = Board([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])

    board.generate(n_gens=2)
