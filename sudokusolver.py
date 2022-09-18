board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

board_empty = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

board_example = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


# Solves grid using backtracking
def solve_grid(grid):
    coord = return_empty(grid)
    if not coord:
        return True

    for i in range(1, 10):
        if check_valid(grid, i, coord):
            grid[coord[0]][coord[1]] = i

            if solve_grid(grid):
                return True

            grid[coord[0]][coord[1]] = 0

    return False


# Check validity of a number being entered at a coordinate in the grid
# Time: O(n^2)
def check_valid(grid, num, coord):
    # assuming that grid is a square
    dim = len(grid)
    # check valid in row
    for i in range(dim):
        if grid[coord[0]][i] == num and coord[1] != i:
            return False

    # check valid in column
    for i in range(dim):
        if grid[i][coord[1]] == num and coord[0] != i:
            return False

    # check valid in 3x3 box
    box_x = coord[1] // 3
    box_y = coord[0] // 3

    for grid_y in range(box_y * 3, box_y * 3 + 3):
        for grid_x in range(box_x * 3, box_x * 3 + 3):
            if grid[grid_y][grid_x] == num and coord != (grid_y, grid_x):
                return False
    return True


# Returns empty coordinate from the grid
# Time: O(n^2)
def return_empty(grid):
    # assuming that grid is a square
    dim = len(grid)
    for grid_y in range(dim):
        for grid_x in range(dim):
            if grid[grid_y][grid_x] == 0:
                coordinate = (grid_y, grid_x)
                return coordinate
    return False


# Prints an image of the grid
# Time: O(n^2)
def print_grid(grid):
    # assuming that grid is a square
    dim = len(grid)
    for grid_y in range(dim):
        if grid_y % 3 == 0 and grid_y != 0:
            print("------------------------")
        for grid_x in range(dim):
            if grid_x % 3 == 0 and grid_x != 0:
                print(" | " + str(grid[grid_y][grid_x]), end=" ")
            else:
                print(str(grid[grid_y][grid_x]), end=" ")
        print("")  # print a new line after each row


# Inputs a valid number into the grid using its coordinates
# Time: O(n)
def input_num(grid, grid_x, grid_y):
    valid_num = False
    while not valid_num:
        try:
            number = int(input("Input number at (" + str(grid_x) + "," + str(grid_y) + "): "))
            if 0 <= number <= 9:
                grid[grid_y][grid_x] = number
                valid_num = True
            elif number == -1:
                print_grid(grid)
            else:
                print("That value entered is not between 0 and 9! please retry")
        except ValueError:
            print("That value entered is not between 0 and 9! please retry")


# Checks if the entered board is valid
# Time O(n^4)
def valid_board(grid):
    dim = len(grid)
    for grid_y in range(dim):
        for grid_x in range(dim):
            if grid[grid_y][grid_x] != 0:
                if not check_valid(grid, grid[grid_y][grid_x], (grid_y, grid_x)):
                    return False
    return True


def main(grid):
    print("Hello! Welcome to this sudoku solver. Here is a version of the blank grid:")
    print_grid(grid)
    print("--------------------------------------")
    print("Instructions:")
    print("1. The coordinate system relative to the grid has the top left corner as (0,0), the top right corner as (8,"
          "0), the bottom left corner as (0,8) and the bottom right corner as (8,8).")
    print("2. Please fill out the the grid according to the prompts based on the coordinate system. If the space is "
          "blank, enter 0.")
    print("3. If you wish to see a visual of the board at any time, please enter -1 instead of the number at the "
          "requested coordinate position.")
    dim = len(grid)
    for grid_y in range(dim):
        for grid_x in range(dim):
            input_num(grid, grid_x, grid_y)
    done_fix = False
    while not done_fix:
        print("Here is copy of your final grid!")
        print_grid(grid)
        try:
            num = int(input("Are there any numbers that need to be replaced? Type 1 if yes and 0 if no: "))
            if num == 0:
                done_fix = True
                break
            number_replace_x = int(input("Please enter the x coordinate of the number you would like to replace: "))
            number_replace_y = int(input("Please enter the y coordinate of the number you would like to replace: "))
            if num == 1 and 0 <= number_replace_x <= 8 and 0 <= number_replace_y <= 8:
                input_num(grid, number_replace_x, number_replace_y)
            else:
                print("One of your values is not valid! please retry (coordinates can only be between 0 and 8, "
                      "values can only be between 0 and 9)")
        except ValueError:
            print("One of your values is not valid! please retry (coordinates can only be between 0 and 8, values can "
                  "only be between 0 and 9)")

    print("Your puzzle:")
    print_grid(grid)
    if not valid_board(grid):
        print("Sorry! The entered puzzle could not be solved!")
        again = int(input("Would you like to solve another sudoku puzzle? Type 1 if yes and 0 if no: "))
        if again == 1:
            grid = board_empty
            main(grid)
    else:
        print("SOLVING......")
        solve_grid(grid)
        print("Solved puzzle:")
        print_grid(grid)
        again = int(input("Would you like to solve another sudoku puzzle? Type 1 if yes and 0 if no: "))
        if again == 1:
            grid = board_empty
            main(grid)


main(board)
