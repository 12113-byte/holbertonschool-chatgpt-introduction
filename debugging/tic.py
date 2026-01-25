def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 5)

def check_winner(board):
    #check rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return True

    #check columns
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True

    #check diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True

    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

def board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_input(player):
    while True:
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if row in [0, 1, 2] and col in [0, 1, 2]:
                return row, col
            else:
                print("Row and column must be 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter valid integers.")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        row, col = get_valid_input(player)
        if board[row][col] != " ":
            print("Cell already taken. Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        #switch player
        player = "O" if player == "X" else "X"

tic_tac_toe()
