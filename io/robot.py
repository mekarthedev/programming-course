#!/usr/bin/python

# Problem: implement programmable robot.

# Displaying field, robot position & orientation.
#  ___________
# |.|.|. . . .|
# |-+-+-
# |.|. . . . .|
# |. . > . . .|
# |. . . . . .|
# |. . . V . .|
# |. . ^ < . .|
#  -----------
# Commands (? for help):

# Command syntax:
# move 4 - move 4 cells forward, back 3 - move 3 cells back
# rotate cw - rotate clock-wise, rotate cc - rotate counter-clock-wise
# cw 90, cw 180, cw 270, cc 90, cc 0
# rotate -90 (counter-clock), rotate +90 (clock-wise)

# Sequence syntax:
# move 4, rotate +90, help, ?, exit, quit
# m4 cw90 exit help ?
