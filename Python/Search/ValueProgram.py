# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def inside_grid(grid, x, y):
    return len(grid) > x >= 0 and len(grid[0]) > y >= 0

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    value = [[ 99 for col in range(len(grid[0]))] for row in range(len(grid))]
    change = True
    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if x == goal[0] and y == goal[1]:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        change = True
                # grid x y is navigatable
                elif grid[x][y] == 0:
                    for i in range(len(delta)):
                        new_x = x + delta[i][0]
                        new_y = y + delta[i][1]
                        if(inside_grid(grid,new_x,new_y)):
                            # new grid is navigatable
                            if grid[new_x][new_y] == 0:
                                v2 = value[new_x][new_y] + cost
                            
                            if v2 < value[x][y]:
                                # print("v1[",x,",",y,"] = ",value[x][y])
                                # print("v2[",new_x,",",new_y,"] = ",v2)
                                change = True
                                value[x][y] = v2

    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    # print(value)
    for i in range(len(value)):
        print(value[i])
    return value 

compute_value(grid,goal,cost)