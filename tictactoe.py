def main():
    board = make_board()
    show_board(board)

def make_board():
    board = []
    for box in range(9):
        board.append(box +1)
    return board

def show_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

if __name__ == "__main__":
    main()