def print_board(board):
    """Prints the current state of the board"""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_win(board, player):
    """Checks if the player has won"""
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False


def check_draw(board):
    """Checks if the game is a draw"""
    return all([cell in ['X', 'O'] for row in board for cell in row])


def get_move(player):
    """Gets a valid move from the player"""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move >= 9:
                print("Invalid move. Please enter a number between 1 and 9.")
            else:
                return divmod(move, 3)
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    """Main function to run the Tic Tac Toe game"""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_move(current_player)

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Cell already taken. Choose another move.")


if __name__ == "__main__":
    main()
