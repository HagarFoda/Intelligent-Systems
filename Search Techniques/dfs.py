board = {1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '}

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")


def space(position):
    if (board[position] == ' '):
        return True
    else:
        return False

# takes a letter (either 'X' or 'O') and a position on the board as input and places the letter at that position.
# It also checks for a winning move after placing the letter and prints a message if a player wins or the game is a draw.
def letter(letter, position):
    if space(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("Draw!")
            exit()
        if checkwin():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()

        return


    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        letter(letter, position)
        return


def checkwin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
#it means that there are still empty positions on the board, and the game is not a draw.
        if (board[key] == ' '):
            return False
    return True


def playerMove():
    position = int(input("Enter the position for 'O':  "))
    letter(player, position)
    return


def compMove():
    bestScore = -800
    bestMove = 0

# Iterate over all empty positions on the board
    for key in board.keys():
        if (board[key] == ' '):

    # Make a temporary move for the computer
            board[key] = bot
    # Evaluate the score for the current board state using the 'dfs' function
            score = dfs(board, 0, False)
    # Undo the temporary move
            board[key] = ' '
    # Update the best score and best move if the current score is better
            if (score > bestScore):
                bestScore = score
                bestMove = key

# Make the best move found by the dfs algorithm
    letter(bot, bestMove)
    return




def dfs(board, depth, maximizing_player):
# Check if the game is over or the depth limit is reached
    if depth == 0 or checkwin():

    # Check if the computer has won
        if checkWhichMarkWon(bot):
            return 1
        
    # Check if the player has won
        elif checkWhichMarkWon(player):
            return -1
    # The game is a draw
        else:
            return 0
        
# Maximizing player (computer)
    if maximizing_player:
        best_score = float('-inf')
    
# Iterate over all empty positions on the board
        for key in board:
            if board[key] == ' ':

            # Make a temporary move for the computer
                board[key] = bot

            # Recursively evaluate the score for the child node
                score = dfs(board, depth - 1, False)
                board[key] = ' '

            # Update the best score
                best_score = max(best_score, score)
        return best_score
    
# Minimizing player (player)
    else:
        best_score = float('inf')
        for key in board:
            if board[key] == ' ':
                board[key] = player
                # Recursively evaluate the score for the child node
                score = dfs(board, depth - 1, True)
                board[key] = ' '
                best_score = min(best_score, score)
        return best_score

'''
def compMove():
    best_score = float('-inf')
    best_move = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = dfs(board, 9, False)  # Assuming depth 9 for the entire board
            board[key] = ' '
            if score > best_score:
                best_score = score
                best_move = key
    letter(bot, best_move)
    return
'''

def playerMove():
    position = int(input("Enter the position for 'O':  "))
    letter(player, position)
    return



printBoard(board)
print("Computer goes first! Good luck.")
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
player = 'O'
bot = 'X'


global firstComputerMove
firstComputerMove = True

while not checkwin():
    compMove()
    playerMove()