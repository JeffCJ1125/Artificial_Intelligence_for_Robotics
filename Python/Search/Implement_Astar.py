# -----------
# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
# 
# If there is no path from init to goal,
# the function should return the string 'fail'
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def inside_grid(grid, x, y):
    return len(grid) > x >= 0 and len(grid[0]) > y >= 0


def search(grid, init, goal, cost,heuristic):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    close_grid = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    expand_direction_list = [
        [0 for col in range(len(grid[0]))] for row in range(len(grid))
    ]
    close_grid[init[0]][init[1]] = 1

    open_node_list = []
    x = init[0]
    y = init[1]
    expand_value = 0
    total_cost_value = expand_value + heuristic[x][y]
    
    open_node_list.append([total_cost_value,expand_value, x, y])
    open_node_list.sort()
    # print(open_node_list)
    found = False
    search_fail = False
    expand_value = 0
    expand_index = 0
    while found == False and search_fail == False:
        if len(open_node_list) == 0:
            search_fail = True
            # print("fail")
            return "fail"
            # return expand
        else:
            open_node_list.sort()
            # print("openList =",open_node_list)
            check_node = open_node_list.pop(0)
            x = check_node[2]
            y = check_node[3]
            node_expand_value = check_node[1]
            node_total_cost_value = check_node[0]
            # expand_direction_list[x][y] = check_node[3]
            expand[x][y] = expand_index
            expand_index += 1
            # print("check node [",x,",",y,"]")
            # Is check node goal?
            if x == goal[0] and y == goal[1]:
                path = [node_total_cost_value,node_expand_value, x, y]
                found = True
            else:
                # add new node into open node list
                node_expand_value += cost
                for step in range(len(delta)):
                    surround_x = x + delta[step][0]
                    surround_y = y + delta[step][1]
                    if inside_grid(grid, surround_x, surround_y):
                        # Is sourrunding node still open and Navigable?
                        if (
                            close_grid[surround_x][surround_y] == 0
                            and grid[surround_x][surround_y] == 0
                        ):
                            node_total_cost_value = node_expand_value + heuristic[surround_x][surround_y]
                            open_node_list.append(
                                [node_total_cost_value,node_expand_value, surround_x, surround_y]
                            )
                            expand_direction_list[surround_x][surround_y] = step
                            close_grid[surround_x][surround_y] = node_expand_value + 1

    # path_direction_list = [
    #     [" " for col in range(len(grid[0]))] for row in range(len(grid))
    # ]
    # # reverse the expand direction from goal
    # path_direction_list[goal[0]][goal[1]] = "*"
    # track_position_x = goal[0]
    # track_position_y = goal[1]
    # delta_index = 0
    # while track_position_x != init[0] or track_position_y != init[1]:
    #     delta_index = expand_direction_list[track_position_x][track_position_y]
    #     track_position_x = track_position_x - delta[delta_index][0]
    #     track_position_y = track_position_y - delta[delta_index][1]
    #     path_direction_list[track_position_x][track_position_y] = delta_name[
    #         delta_index
    #     ]

    # delta_index = expand_direction_list[track_position_x][track_position_y]
    # track_position_x = track_position_x - delta[delta_index][0]
    # track_position_y = track_position_y - delta[delta_index][1]
    # path_direction_list[track_position_x][track_position_y] = delta_name[delta_index]
    # print(path_direction_list)
    return expand
    # return path_direction_list


print(search(grid, init, goal, cost,heuristic))