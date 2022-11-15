# ----- Alex Southwick -----


# ----- Main function -----
def main():
    board = make_board()
    player = player_current("")
    # ----- While loop -----
    while not (player_win(board) or players_tie(board)):
        show_board(board)
        player_turn(player, board)
        player = player_current(player)
    show_board(board)
    print("Good game. Thanks for playing!")

# ----- Function for creating the board boxes -----
def make_board():
    board = []
    for box in range(9):
        board.append(box +1)
    return board

# ----- Function for showing the board to the player -----
def show_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

# ----- Function for alternating player turns each round -----
def player_turn(player, board):
    box = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[box - 1] = player

# ----- Function for finding out who's turn it is (If/Then block) -----
def player_current(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

# ----- Function for ending the game with ALL the possible winning outcomes (I hope) -----
def player_win(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[6] == board[4] == board[2])

# ----- Function for if nobody wins, the game will need to end -----
def players_tie(board):
    for box in range(9):
        if board[box] != "x" and board[box] != "o":
            return False
    return True

# ----- Run that main function -----
if __name__ == "__main__":
    main()