with open("./9/input2.txt") as f:
    lines = f.read().strip().split('\n')
print(lines)

# const for directions
# (x,y)
dirs = {}
dirs['R'] = [0,1]
dirs['L'] = [0,-1]
dirs['U'] = [-1,0]
dirs['D'] = [1,-0]

# RIGHT   = (1,0)
# LEFT    = (-1,0)
# UP      = (0,1)
# DOWN    = (0,-1)

class GridNode:
    tail_visited = False

    def __init__(self, current_symbol: str = '.'):
       self.current_symbol = current_symbol

    def __str__(self):
        return f"{self.current_symbol}"


# Start at bottom left
GRID_SIZE = 10
# grid = [GRID_SIZE][GRID_SIZE]
# for i in range(GRID_SIZE):
#     for j in range(GRID_SIZE):
#         grid[i][j] = GridSymbol()

grid = [[GridNode() for x in range(GRID_SIZE)] for y in range(GRID_SIZE)] 


# print out a representation of each iteration
def print_grid():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            print(f'{grid[i][j]}',end=' ')
        print('')
    print('--------------------------------')

# print out a representation of each iteration
def print_visited_grid():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            print(f"{'#' if grid[i][j].tail_visited else grid[i][j]}",end=' ')
        print('')        


# starting symbol
grid[GRID_SIZE-1][0].current_symbol='s'
grid[GRID_SIZE-1][0].tail_visited = True

head_location = [GRID_SIZE-1,0]
tail_location = [GRID_SIZE-1,0]

# test move right
def move(n: int, dir: str):
    global head_location
    global tail_location
    for i in range(n):
        direction_vec = dirs[dir]
        head_location[0] += direction_vec[0]
        head_location[1] += direction_vec[1]
        # move tail if needed
        y_difference = abs(head_location[0] - tail_location[0])
        x_difference = abs(head_location[1] - tail_location[1])
        if y_difference != x_difference:
            if y_difference > x_difference:
                tail_location[0] = direction_vec[0]
            else:
                tail_location[1] = direction_vec[1]
        else: # diag
            pass
        print(x_difference,y_difference)
        print(head_location)
        print(f'move --> {i+1}')
        print_grid()



move(1,'R')
print_grid()

# print_visited_grid()