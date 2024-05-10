import random

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def make_move(self, row, col):
        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def make_computer_move(self):
        #returns a list of potential moves that would result in a win for the player
        player_wins = self.find_winning_moves('X')
        if player_wins:
            # it means that the player has a winning move available. 
            # The code then randomly selects one of the winning moves from the list and makes it.
            row, col = random.choice(player_wins)
            self.make_move(row, col)
        else:
            computer_wins = self.find_winning_moves('O')
            if computer_wins:
                row, col = random.choice(computer_wins)
                self.make_move(row, col)

            # handles the case where neither the player nor the computer has a winning move available.
            else:
                best_move = self.bidirectional_search()

                #if block checks if the best_move variable is not None. 
                #If it is not, it means that the bidirectional_search function found a good move. 
                # The code then unpacks the best_move tuple into row and col variables and makes the move.
                if best_move:
                    row, col = best_move
                    self.make_move(row, col)
                else:
                    # If no winning move found, make a random move
                    row, col = random.choice(self.get_available_moves())
                    self.make_move(row, col)

    def find_winning_moves(self, player):
        winning_moves = []
#for loops iterate over all the possible positions on the board.
#The range(3) function generates a sequence of numbers from 0 to 2, which represents the rows and columns of the board.
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':

                    #This line temporarily places the player's symbol at the current position on the board.
                    self.board[row][col] = player

# checks if placing the player's symbol at the current position would result in a winning move for the player.
#  If so, the coordinates of the position are appended to the winning_moves list.
                    if self.check_winner(player):
                        winning_moves.append((row, col))

#reverts the change made to the board by setting the position back to an empty space
                    self.board[row][col] = ' '

        return winning_moves

    def bidirectional_search(self):
        available_moves = self.get_available_moves()

# iterates over the list of available moves. 
# For each move, it extracts the row and column, places the computer's symbol ('O') at that position on the board.
        for move in available_moves:
            row, col = move
            self.board[row][col] = 'O'

#checks if placing the computer's symbol at the current position would result in a winning move for the computer. 
# If so, the function immediately returns the coordinates of the move.
            if self.check_winner('O'):
                return move

            self.board[row][col] = ' '

        for move in available_moves:
            row, col = move
            self.board[row][col] = 'X'

#checks if placing the player's symbol at the current position would result in a winning move for the player, 
# or if making this move would lead to a winning move for the computer in the next turn. 
# If either of these conditions is met, the function immediately returns the coordinates of the move.
            if self.check_winner('X') or self.bidirectional_search_helper('O'):
                self.board[row][col] = ' '
                return move

            self.board[row][col] = ' '

        return None

    def bidirectional_search_helper(self, player):
        #This if block checks if the player has a winning move available on the current board. 
        # If so, it immediately returns True, indicating that the player can win in one move.
        if self.check_winner(player):
            return True

        available_moves = self.get_available_moves()

#This for loop iterates over the list of available moves. 
# For each move, it extracts the row and column coordinates and places the current player's symbol (player) 
# at that position on the board.
        for move in available_moves:
            row, col = move
            self.board[row][col] = player

#checks if the current player is the computer ('O'). 
# If so, it calls the bidirectional_search_helper function recursively, 
# passing the player's opponent ('X') as the argument.
#If the recursive call returns False, it means that the player's opponent cannot win in the next move,
# so the current move is a good move for the computer, and the function returns True. 
# Otherwise, the function reverts the change made to the board and returns False.
            if player == 'O':
                if not self.bidirectional_search_helper('X'):
                    self.board[row][col] = ' '
                    return False
            else:

#handles the case where the current player is not the computer ('O'). 
# It is similar to the previous if block, but it checks for a winning move for the computer ('O') in the next move.
                if self.bidirectional_search_helper('O'):
                    self.board[row][col] = ' '
                    return True

            self.board[row][col] = ' '

        if player == 'O':
# the function returns True to indicate that the current move prevents the opponent from winning in the next move.
            return True
        else:
#indicate that the current move does not prevent the opponent from winning in the next move.
            return False

    def get_available_moves(self):
        available_moves = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    available_moves.append((row, col))
        return available_moves

    def check_winner(self, player):
        for row in self.board:
            if row[0] == row[1] == row[2] == player:
                return True

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == player:
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

        return False

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def play(self):
        while True:
            self.print_board()

            if self.check_winner('X'):
                print("Game over. Player wins!")
                break

            if self.check_winner('O'):
                print("Game over. Computer wins!")
                break

            if len(self.get_available_moves()) == 0:
                print("Game over. It's a draw!")
                break

            if self.current_player == 'X':
                row = int(input("Enter the row (0-2): "))
                col = int(input("Enter the column (0-2): "))
                self.make_move(row, col)
            else:
                print("Computer's turn...")
                self.make_computer_move()

        self.print_board()


# Start the game
game = TicTacToe()
game.play()