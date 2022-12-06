# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that
# returns two grids. The first grid, value, should
# contain the computed value of each cell as shown
# in the video. The second grid, policy, should
# contain the optimum policy for each cell.
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.

delta = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # go up  # go left  # go down  # go right

delta_name = ["^", "<", "v", ">"]  # Use these when creating your policy grid.

# ---------------------------------------------
#  Modify the function stochastic_value below
# ---------------------------------------------


def inside_grid(grid, x, y):
    return len(grid) > x >= 0 and len(grid[0]) > y >= 0


def stochastic_value(grid, goal, cost_step, collision_cost, success_prob):
    failure_prob = (
        1.0 - success_prob
    ) / 2.0  # Probability(stepping left) = prob(stepping right) = failure_prob
    value = [
        [collision_cost for col in range(len(grid[0]))] for row in range(len(grid))
    ]
    policy = [[" " for col in range(len(grid[0]))] for row in range(len(grid))]
    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        policy[x][y] = "*"
                        change = True

                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        # for success move , right and left can use for loop to implement.
                        x_move_success = x + delta[a][0]
                        y_move_success = y + delta[a][1]
                        value_success = collision_cost
                        if (
                            inside_grid(grid, x_move_success, y_move_success)
                            and grid[x_move_success][y_move_success] == 0
                        ):
                            value_success = value[x_move_success][y_move_success]
                        left_index = (a + 1) % len(delta)
                        x_move_left = x + delta[left_index][0]
                        y_move_left = y + delta[left_index][1]
                        value_left = collision_cost
                        if (
                            inside_grid(grid, x_move_left, y_move_left)
                            and grid[x_move_left][y_move_left] == 0
                        ):
                            value_left = value[x_move_left][y_move_left]
                        right_index = (a - 1) % len(delta)
                        x_move_right = x + delta[right_index][0]
                        y_move_right = y + delta[right_index][1]
                        value_right = collision_cost
                        if (
                            inside_grid(grid, x_move_right, y_move_right)
                            and grid[x_move_right][y_move_right] == 0
                        ):
                            value_right = value[x_move_right][y_move_right]

                        value_total_cost = (
                            value_success * success_prob
                            + value_left * failure_prob
                            + value_right * failure_prob
                            + cost_step
                        )
                        if value_total_cost < value[x][y]:
                            change = True
                            policy[x][y] = delta_name[a]
                            value[x][y] = value_total_cost
    # print(value)
    return value, policy


# ---------------------------------------------
#  Use the code below to test your solution
# ---------------------------------------------

grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0]]
goal = [0, len(grid[0]) - 1]  # Goal is in top right corner
cost_step = 1
collision_cost = 1000
success_prob = 0.5

value, policy = stochastic_value(grid, goal, cost_step, collision_cost, success_prob)
for row in value:
    print(row)
for row in policy:
    print(row)

# Expected outputs:
#
# [471.9397246855924, 274.85364957758316, 161.5599867065471, 0],
# [334.05159958720344, 230.9574434590965, 183.69314862430264, 176.69517762501977],
# [398.3517867450282, 277.5898270101976, 246.09263437756917, 335.3944132514738],
# [700.1758933725141, 1000, 1000, 668.697206625737]


#
# ['>', 'v', 'v', '*']
# ['>', '>', '^', '<']
# ['>', '^', '^', '<']
# ['^', ' ', ' ', '^']
