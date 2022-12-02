# Empty Cell
# print(0.75 ** 1)
# print(0.75 ** 4)
# print(0.75 ** 10)


# Motion Question
grid = [[5, 3], [3, 1]]

# new_grid = []
for step in range(10):
    new_grid = [[0.0 for col in range(len(grid[0]))] for row in range(len(grid))]
    for y in range(len(grid)):
        move_vertical_y_index = (y + 1) % len(grid)
        move_horizon_y_index = y
        for x in range(len(grid[0])):
            move_horizon_x_index = (x + 1) % len(grid[0])
            move_vertical_x_index = x
            new_grid[move_horizon_y_index][move_horizon_x_index] += grid[y][x] * 0.5
            new_grid[move_vertical_y_index][move_vertical_x_index] += grid[y][x] * (
                1 - 0.5
            )
    grid = new_grid
    print(grid)
