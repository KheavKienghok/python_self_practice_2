class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def make_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True  # Return True if move is successful
        else:
            return False  # Return False if move is invalid

    def check_win(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def display_board(self):
        for row in self.board:
            print(' | '.join(row))
            print('--' * 5)

def main() -> None:
    game = TicTacToe()

    for _ in range(3):
        game.display_board()
        ask_row = int(input("Enter the row: "))
        ask_column = int(input("Enter the column: "))
        
        # Check if the player's move is valid
        while not game.make_move(ask_row, ask_column):
            print("Invalid move. Try again.")
            ask_row = int(input("Enter the row: "))
            ask_column = int(input("Enter the column: "))
        
        # Check for a win after the player's move
        if game.check_win():
            print("You win!")
            break
        
        # Bot's turn (assuming a random move)
        # You need a strategy here to make the bot's move, this is just a placeholder
        bot_choice_row = 1
        bot_choice_column = 1
        game.make_move(bot_choice_row, bot_choice_column)
        
        # Check for a win after the bot's move
        if game.check_win():
            print("Bot wins!")
            break

if __name__ == "__main__":
    main()