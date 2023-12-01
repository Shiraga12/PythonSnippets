def is_valid_sudoku(board):
    # Check rows
    for row in board:
        if not is_valid_set(row):
            return "No"

    # Check columns
    for col in zip(*board):
        if not is_valid_set(col):
            return "No"

    # Check sub-squares
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_set(sub_square):
                return "No"

    return "Yes"

def is_valid_set(lst):
    # Check if a list contains all digits from 1 to 9
    return set(lst) == set(range(1, 10))

# Read the Sudoku board from user input
sudoku_board = [list(map(int, input())) for _ in range(9)]

# Check if the Sudoku is valid and print the result
print(is_valid_sudoku(sudoku_board))
