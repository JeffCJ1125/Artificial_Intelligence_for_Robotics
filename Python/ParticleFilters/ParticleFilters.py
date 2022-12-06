# Now we want to create particles,
# p[i] = robot(). In this assignment, write
# code that will assign 1000 such particles
# to a list.
#
# Your program should print out the length
# of your list (don't cheat by making an
# arbitrary list of 1000 elements!)
#

from RobotClass import robot
from RobotClass import eval
import math
import random

myrobot = robot()

N = 1000
p = []

for i in range(N):
    x = robot()
    x.set_noise(0.05, 0.05, 5.0)
    p.append(x)
# Now we want to simulate robot
# motion with our particles.
# Each particle should turn by 0.1
# and then move by 5.
Test = 10
print(eval(myrobot, p))
for test in range(Test):
    myrobot = myrobot.move(0.1, 5.0)
    Z = myrobot.sense()

    for i in range(N):
        p[i] = p[i].move(0.1, 5)
    # Now we want to give weight to our
    # particles. This program will print a
    # list of 1000 particle weights.
    w = []
    for i in range(N):
        w.append(p[i].measurement_prob(Z))

    # In this exercise, try to write a program that
    # will resample particles according to their weights.
    # Particles with higher weights should be sampled
    # more frequently (in proportion to their weight).

    pick_index = int(random.random() * N)
    # print(pick_index)
    pick_weight = 0
    max_weight = max(w)
    p3 = []
    the_index = []
    for i in range(N):
        pick_weight += random.random() * 2 * max_weight
        # print("i",i,"begin index :",pick_index)
        # print("pick_weight = ",pick_weight, "w[",pick_index,"]=",w[pick_index])
        while pick_weight > w[pick_index]:
            pick_weight -= w[pick_index]
            pick_index = (pick_index + 1) % N
        # print("take index :",pick_index)
        the_index.append(pick_index)
        p3.append(p[pick_index])
    p = p3
    print(eval(myrobot, p))
