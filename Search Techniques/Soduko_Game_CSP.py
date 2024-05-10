# Import required libraries
import random
from copy import deepcopy

# Define the Sudoku board size
BOARD_SIZE = 9

# Function to print the Sudoku board
def print_board(board):
    for i in range(BOARD_SIZE):
        # Print horizontal separator after every 3 rows, except for the first row
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(BOARD_SIZE):
            # Print vertical separator after every 3 columns, except for the first column
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            # Print the value at the current cell
            print(board[i][j], end=" ")
        # Move to the next line after printing each row
        print()

#checks if placing a specific number num in a particular position (row, col) in the Sudoku board board is valid.
def is_valid(board, row, col, num):

#iterates through the entire row row and checks if the number num already exists in any cell of that row. 
# If it does, it means placing num in the current position (row, col) would violate the rule
# so the function returns False immediately.
    for i in range(BOARD_SIZE):
        if board[row][i] == num:
            return False

    # Check the column
    for i in range(BOARD_SIZE):
        if board[i][col] == num:
            return False

    # Check the 3x3 box
    box_row = (row // 3) * 3  # Calculate the starting row index of the 3x3 box
    box_col = (col // 3) * 3  # Calculate the starting column index of the 3x3 box
    for i in range(3):
        for j in range(3):
            #This checks if the value num already exists within the 3x3 box. If it does,
            # it means the value is invalid in the current position, so the function returns False.
            if board[box_row + i][box_col + j] == num:
                return False

    return True

# Function to solve the Sudoku puzzle using backtracking and CSP
def solve_sudoku(board):
    for row in range(BOARD_SIZE):  # Iterate over each row of the Sudoku board
        for col in range(BOARD_SIZE):  # Iterate over each column of the Sudoku board
            if board[row][col] == 0:  # Check if the current cell is empty (contains 0)
                for num in range(1, 10):  # Try each number from 1 to 9 in the current cell
                    if is_valid(board, row, col, num):  # Check if the number is valid in the current position
                        board[row][col] = num  # Assign the valid number to the current cell
                        if solve_sudoku(board):  # Recursively solve the Sudoku puzzle with the updated board
                            return True  # If the puzzle is solved, return True
                        board[row][col] = 0  # If the puzzle is not solved, backtrack by resetting the current cell to 0
                return False  # If no valid number can be placed in the current cell, return False
    return True  # If all cells are filled with valid numbers, the puzzle is solved, so return True

# Function to generate a Sudoku puzzle
def generate_sudoku(difficulty):
    # Create an empty Sudoku board
    board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    
#This line calls the solve_sudoku function to solve the Sudoku puzzle on the empty board. 
# This ensures that the initial state of the puzzle is a valid solution.
    solve_sudoku(board)
    
    # Remove random cells based on the difficulty level
    num_cells_to_remove = difficulty * 10  # Calculate the number of cells to remove based on the difficulty level
    # The difficulty level is multiplied by 10 to adjust the number of cells removed proportionally.

#iterates the specified number of times (determined by num_cells_to_remove) to remove cells from the solved Sudoku board.
# For each iteration, it generates random row and column indices within the board size 
# and sets the value of the corresponding cell to 0, effectively removing the number from that position. 

    for _ in range(num_cells_to_remove):  # Iterate the specified number of times to remove cells
        row = random.randint(0, BOARD_SIZE - 1)  # Generate a random row index within the board size
        col = random.randint(0, BOARD_SIZE - 1)  # Generate a random column index within the board size
        board[row][col] = 0  # Set the value of the randomly chosen cell to 0 (remove the value)

    return board  # Return the modified board with cells removed

# Main function
def main():
    # Generate a Sudoku puzzle with the desired difficulty level
    difficulty = int(input("Enter the difficulty level (1-5): "))
    board = generate_sudoku(difficulty)
    
    # Print the initial Sudoku board
    print("Initial Sudoku Board:")
    print_board(board)
    
    # Solve the Sudoku puzzle
    board_copy = deepcopy(board)
    solve_sudoku(board_copy)
    
    # Print the solved Sudoku board
    print("\nSolved Sudoku Board:")
    print_board(board_copy)

# Run the main function
if __name__ == "__main__":
    main()