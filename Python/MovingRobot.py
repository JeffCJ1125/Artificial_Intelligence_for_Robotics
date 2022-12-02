# Make a robot called myrobot that starts at
# coordinates 30, 50 heading north (pi/2).
# Have your robot turn clockwise by pi/2, move
# 15 m, and sense. Then have it turn clockwise
# by pi/2 again, move 10 m, and sense again.

#
# Your program should print out the result of
# your two sense measurements.
#

from RobotClass import robot
import math

myrobot = robot()
# print(myrobot)
myrobot.set(30, 50, math.pi / 2)
# print(myrobot)
myrobot = myrobot.move(-1.0 * math.pi / 2, 15)
# print(myrobot)
print(myrobot.sense())
myrobot = myrobot.move(-1.0 * math.pi / 2, 10)
# print(myrobot)
print(myrobot.sense())
# print(myrobot)
