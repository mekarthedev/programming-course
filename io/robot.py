#!/usr/bin/python

# Problem: implement programmable robot.

# Displaying field, robot position & orientation.
#  _____________
# | . . . . . . |
# | . . . . . . |
# | . . > . . . |
# | . . . . . . |
# | . . . v . . |
# | . . ^ < . . |
#  -------------
# Commands (? for help):

# Command syntax:
# move 4 - move 4 cells forward, back 3 - move 3 cells back
# rotate cw - rotate clock-wise, rotate cc - rotate counter-clock-wise
# cw 90, cw 180, cw 270, cc 90, cc 0
# rotate -90 (counter-clock), rotate +90 (clock-wise)

# Sequence syntax:
# move 4, rotate +90, help, ?, exit, quit
# m4 cw90 exit help ?

import math

def testEqual(actualResult, expectedResult):
   if actualResult == expectedResult:
      print "passed"
   else:
      print "failed, expected " + str(expectedResult) + ", returned " + str(actualResult)

# Canvas
# - create canvas WxH size
# - set symbol at point X,Y
# - get symbol at point X,Y
# - get canvas width
# - get canvas height

def createCanvas(width, height):
   rowsNumber = 0
   canvas = []
   while rowsNumber < height:
      rowSymbolsNumber = 0
      row = []
      while rowSymbolsNumber < width:
         row.append(None)
         rowSymbolsNumber = rowSymbolsNumber + 1
      canvas.append(row)
      rowsNumber = rowsNumber + 1
   return canvas

def getCanvasWidth(canvas):
   return len(canvas[0])

def getCanvasHeight(canvas):
   return len(canvas)

def setSymbolAtPoint(canvas, x, y, symbol):
   canvas[y][x] = symbol

def getSymbolAtPoint(canvas, x, y):
   return canvas[y][x]

canvas = createCanvas(3, 4)
testEqual(getCanvasWidth(canvas), 3)
testEqual(getCanvasHeight(canvas), 4)
setSymbolAtPoint(canvas, 1, 2, ".")
testEqual(getSymbolAtPoint(canvas, 1, 2), ".")

def printCanvas(canvas):
   y = 0
   while y < getCanvasHeight(canvas):
      x = 0
      row = ""
      while x < getCanvasWidth(canvas):
         row = row + str(getSymbolAtPoint(canvas, x, y))
         x = x + 1
      print row
      y = y + 1

# Draw scene

def drawBorder(canvas, x, y, width, height):

   # drawing border top and bottom      
   xCanvas = x + 1
   while xCanvas < x + width - 1:
      setSymbolAtPoint(canvas, xCanvas, y, "_")
      setSymbolAtPoint(canvas, xCanvas, y + height - 1, "-")
      xCanvas = xCanvas + 1

   # drawing border sides
   yCanvas = y + 1
   while yCanvas < y + height - 1:
      setSymbolAtPoint(canvas, x, yCanvas, "|")
      setSymbolAtPoint(canvas, x + width - 1, yCanvas, "|")
      yCanvas = yCanvas + 1

def clearCanvas(canvas):
   yCanvas = 0
   while yCanvas < getCanvasHeight(canvas):     
      xCanvas = 0
      while xCanvas < getCanvasWidth(canvas):
         setSymbolAtPoint(canvas, xCanvas, yCanvas, " ")
         xCanvas = xCanvas + 1
      yCanvas = yCanvas + 1

def drawCells(canvas, x, y, width, height):
   yCanvas = y
   while yCanvas < y + height:
      xCanvas = x + 1
      while xCanvas < x + width - 1:
         setSymbolAtPoint(canvas, xCanvas, yCanvas, ".")
         xCanvas = xCanvas + 2
      yCanvas = yCanvas + 1

def drawRobot(canvas, x, y, direction):
   if direction % 360 == 90:
      robotSymbol = ">"
   elif direction % 360 == 270:
      robotSymbol = "<"
   elif direction % 360 == 0:
      robotSymbol = "^"
   elif direction % 360 == 180:
      robotSymbol = "v"
   setSymbolAtPoint(canvas, x, y, robotSymbol)

print "****"
canvas = createCanvas(10, 10)
drawRobot(canvas, 1, 2, 90)
testEqual(getSymbolAtPoint(canvas, 1, 2), ">")
drawRobot(canvas, 1, 2, -9090)
testEqual(getSymbolAtPoint(canvas, 1, 2), "<")
   
def drawField(canvas, x, y, width, height):
   borderWidth = 2*width + 3
   borderHeight = height + 2
   drawBorder(canvas, x, y, borderWidth, borderHeight)
   drawCells(canvas, x + 1, y + 1, borderWidth - 2, borderHeight - 2)

def cellPositionInPixels(robotX, robotY, fieldX, fieldY):
   return (fieldX + 2 + 2*robotX, fieldY + 1 + robotY)
   
testEqual(cellPositionInPixels(1, 2, 10, 15), (14, 18))

def fieldSizeInPixels(width, height):
   return (2 * width + 3, height + 2)

testEqual(fieldSizeInPixels(4, 3), (11, 5))

def drawScene(fieldWidth, fieldHeight, robotX, robotY, robotDirection):
   (canvasWidth, canvasHeight) = fieldSizeInPixels(fieldWidth, fieldHeight)
   canvas = createCanvas(canvasWidth, canvasHeight)
   clearCanvas(canvas)
   drawField(canvas, 0, 0, fieldWidth, fieldHeight)
   (robotXInPixels, robotYInPixels) = cellPositionInPixels(robotX, robotY, 0, 0)
   drawRobot(canvas, robotXInPixels, robotYInPixels, robotDirection)
   printCanvas(canvas)


# Robot model

def createRobot(initialX, initialY, initialDirection):
   return [initialX, initialY, initialDirection, []]

def getRobotPosition(robot):
   return (robot[0], robot[1])

def getRobotDirection(robot):
   return robot[2]

def rotateRobot(robot, angle):
   robot[2] = (angle + getRobotDirection(robot)) % 360
   notifyRobotSubscribers(robot)

def moveRobot(robot, distance):
   robot[0] = int(round(robot[0] + distance * math.sin(math.radians(robot[2]))))
   robot[1] = int(round(robot[1] - distance * math.cos(math.radians(robot[2]))))
   notifyRobotSubscribers(robot)
   
def subscribeToRobotStateChange(robot, stateChangeHandler):
   robot[3].append(stateChangeHandler)

def notifyRobotSubscribers(robot):
   if robot[3] != []:
      elementNumber = 0
      while elementNumber < len(robot[3]):
         robot[3][elementNumber](robot)
         elementNumber = elementNumber + 1
   
robot = createRobot(1, 2, 180)
testEqual(getRobotPosition(robot), (1, 2))
testEqual(getRobotDirection(robot), 180)

print "---"

robot = createRobot(1, 2, 180)
rotateRobot(robot, 180)
testEqual(getRobotDirection(robot) % 360, 0)
rotateRobot(robot, 90)
testEqual(getRobotDirection(robot) % 360, 90)
rotateRobot(robot, 180)
testEqual(getRobotDirection(robot) % 360, 270)
rotateRobot(robot, -90)
testEqual(getRobotDirection(robot) % 360, 180)

print "---"

robot = createRobot(1, 2, 0)
moveRobot(robot, 1)
testEqual(getRobotPosition(robot), (1, 1))

rotateRobot(robot, 90)
moveRobot(robot, 2)
testEqual(getRobotPosition(robot), (3, 1))

rotateRobot(robot, 180)
moveRobot(robot, 1)
testEqual(getRobotPosition(robot), (2, 1))

rotateRobot(robot, -90)
moveRobot(robot, 2)
testEqual(getRobotPosition(robot), (2, 3))

rotateRobot(robot, 30)
moveRobot(robot, 50)
testEqual(getRobotPosition(robot), (-23, 46))

print "---"

direction = None
position = None
publishingRobot = None
def onTestRobotChange(robot):
   global direction
   global position
   global publishingRobot
   direction = getRobotDirection(robot)
   position = getRobotPosition(robot)
   publishingRobot = robot
   
robot1 = createRobot(1, 2, 0)
subscribeToRobotStateChange(robot1, onTestRobotChange)
rotateRobot(robot1, 90)
testEqual(direction, 90)
testEqual(publishingRobot, robot1)

robot2 = createRobot(1, 2, 90)
subscribeToRobotStateChange(robot2, onTestRobotChange)
moveRobot(robot2, 42)
testEqual(position, (43, 2))
testEqual(publishingRobot, robot2)

#

import time

def drawRobotState(robot):
   (robotX, robotY) = getRobotPosition(robot)
   robotDirection = getRobotDirection(robot)
   drawScene(44, 44, robotX, robotY, robotDirection)
   time.sleep(0.25)


robot = createRobot(0, 0, 180)
drawRobotState(robot)
subscribeToRobotStateChange(robot, drawRobotState)
moveRobot(robot, 1)
moveRobot(robot, 1)
moveRobot(robot, 1)
rotateRobot(robot, -90)
moveRobot(robot, 1)
moveRobot(robot, 1)
moveRobot(robot, 1)
moveRobot(robot, 1)
rotateRobot(robot, 90)
moveRobot(robot, 1)
moveRobot(robot, 1)
moveRobot(robot, 1)
moveRobot(robot, 1)
rotateRobot(robot, 90)
moveRobot(robot, 1)
rotateRobot(robot, 90)
moveRobot(robot, 1)
rotateRobot(robot, 90)
moveRobot(robot, 1)
rotateRobot(robot, 90)
moveRobot(robot, 1)
