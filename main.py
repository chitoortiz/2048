import random

def start_game():
 
    # declaring an empty list then
    # appending 4 list each with four
    # elements as 0.
    board =[]
    for i in range(4):
        board.append([0] * 4)
 
    # calling the function to add
    # a new 2 in grid after every step
    add_two(board)
    return board

def add_two(mat):
 
    r = random.randint(0, 3)
    c = random.randint(0, 3)
 
    while(mat[r][c] != 0):
        r = random.randint(0, 3)
        c = random.randint(0, 3)
 
    mat[r][c] = 2

# Compress board to the left before and after merging cells
def compress(mat):
 
    changed = False
 
    new_mat = []
 
    for i in range(4):
        new_mat.append([0] * 4)
         
    for i in range(4):
        pos = 0
 
        for j in range(4):
            if(mat[i][j] != 0):
                 
                new_mat[i][pos] = mat[i][j]
                 
                if(j != pos):
                    changed = True
                pos += 1

    for i in range(4):
        print(new_mat[i])
    print("")
    return new_mat, changed

# Adds horizontal neighbours together
def merge(mat):
     
    changed = False
     
    for i in range(4):
        for j in range(3):
 
            if(mat[i][j] == mat[i][j + 1] and mat[i][j] != 0):
 
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
 
                changed = True
 
    for i in range(4):
        print(mat[i])
    print("")
    return mat, changed

# Flips rows
def reverse(mat):
    new_mat =[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3 - j])
    for i in range(4):
        print(new_mat[i])
    print("")
    return new_mat
    
# Swaps rows and columns
def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    for i in range(4):
        print(new_mat[i])
    print("")
    return new_mat

def move_left(grid):
 
    new_grid, changed1 = compress(grid)
 
    new_grid, changed2 = merge(new_grid)
     
    changed = changed1 or changed2
 
    new_grid, temp = compress(new_grid)
 
    for i in range(4):
        print(new_grid[i])
    print("")
    return new_grid, changed

def move_right(grid):
 
    new_grid = reverse(grid)
 
    new_grid, changed = move_left(new_grid)
 
    new_grid = reverse(new_grid)

    for i in range(4):
        print(new_grid[i])
    print("")
    return new_grid, changed

def move_up(grid):
 
    new_grid = transpose(grid)
 
    new_grid, changed = move_left(new_grid)
 
    new_grid = transpose(new_grid)

    for i in range(4):
        print(new_grid[i])
    print("")
    return new_grid, changed

def move_down(grid):
 
    new_grid = transpose(grid)
 
    new_grid, changed = move_right(new_grid)
 
    new_grid = transpose(new_grid)

    for i in range(4):
        print(new_grid[i])
    print("")
    return new_grid, changed

def get_current_state(mat):
 
    # if any cell contains
    # 2048 we have won
    for i in range(4):
        for j in range(4):
            if(mat[i][j]== 2048):
                return 'WON'
 
    # if we are still left with
    # atleast one empty cell
    # game is not yet over
    for i in range(4):
        for j in range(4):
            if(mat[i][j]== 0):
                return 'GAME NOT OVER'
 
    # or if no cell is empty now
    # but if after any move left, right,
    # up or down, if any two cells
    # gets merged and create an empty
    # cell then also game is not yet over
    for i in range(3):
        for j in range(3):
            if(mat[i][j]== mat[i + 1][j] or mat[i][j]== mat[i][j + 1]):
                return 'GAME NOT OVER'
 
    for j in range(3):
        if(mat[3][j]== mat[3][j + 1]):
            return 'GAME NOT OVER'
 
    for i in range(3):
        if(mat[i][3]== mat[i + 1][3]):
            return 'GAME NOT OVER'
 
    # else we have lost the game
    return 'LOST'

board = start_game()

# Game loop
playing = True
while playing:
    x = input("What move? (up/down/left/right) ")

    if x == 'up':
        board, flag = move_up(board)
        status = get_current_state(board)
        if status == 'GAME NOT OVER':
            add_two(board)
        else:
            break

    elif x == 'down':
        board, flag = move_down(board)
        status = get_current_state(board)
        if status == 'GAME NOT OVER':
            add_two(board)
        else:
            break

    elif x == 'left':
        board, flag = move_left(board)
        status = get_current_state(board)
        if status == 'GAME NOT OVER':
            add_two(board)
        else:
            break

    elif x == 'right':
        board, flag = move_right(board)
        status = get_current_state(board)
        if status == 'GAME NOT OVER':
            add_two(board)
        else:
            break

    else:
        print("wtf")

    for i in range(4):
        print(board[i])

