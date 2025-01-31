import os

logo = r'''
___         ___         ___      
 |  o  _     |  _  _     |  _  _ 
 |  | (_     | (_|(_     | (_)(/_

'''

# clears the terminal screen to continue
def clear_screen():
    if os.name == 'nt':     # Windows
        os.system('cls')
    else:                   # macOS or Linux
        os.system('clear')

# print the current board
def print_board(board):
    print("    1   2   3")                              # number for row
    print("  +---+---+---+")
    for i, row in enumerate(board):
        print(f"{i + 1} | " + " | ".join(row) + " |")   # number for column and row(array)
        print("  +---+---+---+")


# play with computer or another person
def select_mode():
    while True:
        mode = input("Select the mode (1p / 2p): ").strip().upper()
        if mode.upper() == "1P":
            return ["human", "computer"]
        elif mode.upper() == "2P":
            return ["player1", "player2"]
        else:
            print("Invalid input. Please select '1p' or '2p'.\n")

# choose the player will take first turn
def select_turn(players):
    while True:
        turn = input(f"Who starts first? Enter 1 for {players[0]} / 2 for {players[1]}: ")
        if turn == "1":
            return players[0]
        elif turn == "2":
            return players[1]
        else:
            print("Invalid input. Please select '1' or '2'.\n")

# select the available spot on the board
def select_spot(board, player, mark):
    while True:
        spot = input(f"{player}'s turn: ").strip()
        if spot == "0 0":
            print("😵 Exit the game.")
            return False
        elif spot[0].isdigit() and 1 <= int(spot[0]) <= 3 and \
             spot[1] == " " and \
             spot[2].isdigit() and 1 <= int(spot[2]) <= 3:
            if board[int(spot[0]) - 1][int(spot[2]) - 1] == " ":
                board[int(spot[0]) - 1][int(spot[2]) - 1] = mark
                return board
            else:
                print("That spot is already taken. Try again!")
        else:
            print("Invalid input.")

# check if it's the draw situation
def is_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    clear_screen()
    print(logo)
    print_board(board)
    print("😐 It's a draw...")
    return True

# check if it's the winning situation
def is_win(board, player, mark):
    if board[0][0] == board[0][1] == board[0][2] == mark or \
       board[1][0] == board[1][1] == board[1][2] == mark or \
       board[2][0] == board[2][1] == board[2][2] == mark or \
       board[0][0] == board[1][0] == board[2][0] == mark or \
       board[0][1] == board[1][1] == board[2][1] == mark or \
       board[0][2] == board[1][2] == board[2][2] == mark or \
       board[0][0] == board[1][1] == board[2][2] == mark or \
       board[0][2] == board[1][1] == board[2][0] == mark:
        clear_screen()
        print(logo)
        print_board(board)
        print(f"🥳 {player} wins!")
        return True
    else:
       return False

# Game loop
def game_play():

    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    print(logo)
    print_board(board)

    players = select_mode()
    if select_turn(players) == players[0]:
        current_turn = players[0]
        current_mark = "O"
    else:
        current_turn = players[1]
        current_mark = "X"

    is_game_over = False
    while not is_game_over:
        clear_screen()
        print(logo)
        print_board(board)
        print(f"[ {players[0]}: O | {players[1]}: X ]\n")

        board = select_spot(board, current_turn, current_mark)
        
        if not board or is_draw(board) or is_win(board, current_turn, current_mark):
            is_game_over = True
        else:
            if current_turn == players[0]:
                current_turn = players[1]
                current_mark = "X"
            else:
                current_turn = players[0]
                current_mark = "O"

    

game_play()