# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth,
# and tolerance) and returns a smooth path. The first and
# last points should remain unchanged.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the instructor's note
# below (the equations given in the video are not quite
# correct).
# -----------

from copy import deepcopy
import math

# thank you to EnTerr for posting this on our discussion forum


def printpaths(path, newpath):
    for old, new in zip(path, newpath):
        print(
            "["
            + ", ".join("%.3f" % x for x in old)
            + "] -> ["
            + ", ".join("%.3f" % x for x in new)
            + "]"
        )


# Don't modify path inside your function.
path = [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [4, 3], [4, 4]]


def smooth(path, weight_data=0.5, weight_smooth=0.1, tolerance=0.000001):

    # Make a deep copy of path into newpath
    newpath = [[0, 0] for i in range(len(path))]

    #######################
    ### ENTER CODE HERE ###
    #######################
    # for update_time in range(3):
    for i in range(len(path)):
        newpath[i][0] = path[i][0]
        newpath[i][1] = path[i][1]

    update_dif = 1
    update_time = 0
    while update_dif > tolerance:
        update_dif = 0
        update_time += 1
        for i in range(len(newpath)):
            # Contraint
            # find the vector of yi to xi is minmum.
            # find the vector of yi to y_last is minmum.
            # find the vector of yi to y_next is minmum.
            # Contraint function F(yi)  = alpha(xi - yi)**2 + beta(yi_next - yi)**2 + beta(yi_last - yi)**2
            # use Gradient descent to found minum F(yi)
            # new_yi <- yi + alpha (xi - yi) + beta (yi_next + y_last - 2 * yi)
            if i > 0 and i < len(path) - 1:
                yi_x = newpath[i][0]
                yi_next_x = newpath[i + 1][0]
                yi_last_x = newpath[i - 1][0]
                xi_x = path[i][0]
                n_x = (
                    yi_x
                    + weight_data * (xi_x - yi_x)
                    + weight_smooth * (yi_next_x + yi_last_x - 2 * yi_x)
                )
                yi_y = newpath[i][1]
                yi_next_y = newpath[i + 1][1]
                yi_last_y = newpath[i - 1][1]
                xi_y = path[i][1]
                n_y = (
                    yi_y
                    + weight_data * (xi_y - yi_y)
                    + weight_smooth * (yi_next_y + yi_last_y - 2 * yi_y)
                )

                update_dif += math.fabs(newpath[i][0] - n_x) + math.fabs(
                    newpath[i][1] - n_y
                )
                newpath[i][0] = n_x
                newpath[i][1] = n_y

        # print("update ",update_time,"dif",update_dif)
    return newpath  # Leave this line for the grader!


printpaths(path, smooth(path))
