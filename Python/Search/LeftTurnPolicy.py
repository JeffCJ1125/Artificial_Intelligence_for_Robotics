# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

forward = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # go up  # go left  # go down  # go right
forward_name = ["up", "left", "down", "right"]

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ["R", "#", "L"]

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [
    [1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1],
]

init = [4, 3, 0]  # given in the form [row,col,direction]
# direction = 0: up
#             1: left
#             2: down
#             3: right

goal = [2, 0]  # given in the form [row,col]

cost = [2, 1, 15]  # cost has 3 values, corresponding to making
# a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------


def inside_grid(grid, x, y):
    return len(grid) > x >= 0 and len(grid[0]) > y >= 0


def optimum_policy2D(grid, init, goal, cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    value = [
        [[999 for row in range(len(grid[0]))] for col in range(len(grid))]
        for ori in range(4)
    ]
    policy = [
        [[" " for col in range(len(grid[0]))] for row in range(len(grid))]
        for ori in range(4)
    ]
    change = True

    while change:
        change = False
        for ori in range(len(value)):
            for x in range(len(grid)):
                for y in range(len(grid[0])):
                    if goal[0] == x and goal[1] == y:
                        if value[ori][x][y] > 0:
                            value[ori][x][y] = 0
                            policy[ori][x][y] = "*"
                            change = True

                    elif grid[x][y] == 0:
                        for a in range(len(action)):
                            new_ori = (ori + action[a]) % 4
                            x2 = x + forward[new_ori][0]
                            y2 = y + forward[new_ori][1]

                            if (
                                x2 >= 0
                                and x2 < len(grid)
                                and y2 >= 0
                                and y2 < len(grid[0])
                                and grid[x2][y2] == 0
                            ):
                                v2 = value[new_ori][x2][y2] + cost[a]

                                if v2 < value[ori][x][y]:
                                    change = True
                                    policy[ori][x][y] = action_name[a]
                                    value[ori][x][y] = v2
    # print(value)
    # reverse the expand direction from goal
    # policy2D[goal[0]][goal[1]] = "*"
    track_position_x = init[0]
    track_position_y = init[1]
    track_head = init[2]
    delta_index = 0
    policy2D = [[" " for col in range(len(grid[0]))] for row in range(len(grid))]
    policy2D[track_position_x][track_position_y] = policy[track_head][track_position_x][
        track_position_y
    ]
    while policy[track_head][track_position_x][track_position_y] != "*":
        track_action = policy[track_head][track_position_x][track_position_y]
        if track_action == "R":
            track_head = (track_head + action[0]) % 4
        elif track_action == "#":
            track_head = track_head
        elif track_action == "L":
            track_head = (track_head + action[2]) % 4
        # print("old",track_position_x,track_position_y)
        track_position_x = track_position_x + forward[track_head][0]
        track_position_y = track_position_y + forward[track_head][1]
        # print("new",track_position_x,track_position_y)
        policy2D[track_position_x][track_position_y] = policy[track_head][
            track_position_x
        ][track_position_y]
    return policy2D


print(optimum_policy2D(grid, init, goal, cost))
