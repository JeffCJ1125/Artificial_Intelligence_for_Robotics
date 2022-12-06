# Now add noise to your robot as follows:
# forward_noise = 5.0, turn_noise = 0.1,
# sense_noise = 5.0.
#
# Once again, your robot starts at 30, 50,
# heading north (pi/2), then turns clockwise
# by pi/2, moves 15 meters, senses,
# then turns clockwise by pi/2 again, moves
# 10 m, then senses again.
#
# Your program should print out the result of
# your two sense measurements.

from RobotClass import robot
import math

myrobot = robot()
# print(myrobot)
myrobot.set_noise(5.0, 0.1, 5.0)
myrobot.set(30, 50, math.pi / 2)
# print(myrobot)
myrobot = myrobot.move(-1.0 * math.pi / 2, 15)
# print(myrobot)
print(myrobot.sense())
myrobot = myrobot.move(-1.0 * math.pi / 2, 10)
# print(myrobot)
print(myrobot.sense())
