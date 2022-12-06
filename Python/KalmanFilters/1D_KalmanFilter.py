import math

# Write a program that will iteratively update and
# predict based on the location measurements
# and inferred motions shown below.


def update(mean1, var1, mean2, var2):
    new_mean = 1 / (var1 + var2) * (var2 * mean1 + var1 * mean2)
    new_var = 1 / (1 / var1 + 1 / var2)
    return [new_mean, new_var]


def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]


measurements = [5.0, 6.0, 7.0, 9.0, 10.0]
motion = [1.0, 1.0, 2.0, 1.0, 1.0]
measurement_sig = 4.0
motion_sig = 2.0
mu = 0.0
sig = 10000.0

# Please print out ONLY the final values of the mean
# and the variance in a list [mu, sig].

# Insert code here
for i in range(len(measurements)):
    [mu, sig] = update(mu, sig, measurements[i], measurement_sig)
    [mu, sig] = predict(mu, sig, motion[i], motion_sig)

print([mu, sig])
