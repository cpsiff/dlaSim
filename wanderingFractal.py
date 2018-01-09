from graphics import *
import random
import math
import os

WIN_W = 1024
WIN_H = 1024
RENDER_SCALE = 8
ITERATIONS = 400
SPACING = 2
RENDER_RATIO = int(WIN_W/RENDER_SCALE)


#Used to clear console during loading bar
def clear():
    os.system( 'cls' )


def drawGrid(pixelList):
    erase = Rectangle(Point(0,0),Point(WIN_W, WIN_H))
    erase.setFill("white")
    erase.draw(win)
    #color each cell its corresponding color
    for i in range (len(pixelList)):
        for j in range(len(pixelList[0])):
            if pixelList[i][j] != 0:
                rect = Rectangle(Point(RENDER_SCALE * i, RENDER_SCALE * j),
                                 Point(RENDER_SCALE * i + RENDER_SCALE, RENDER_SCALE * j + RENDER_SCALE))
                if pixelList[i][j] == 1:
                    rect.setFill("black")
                    rect.setOutline("black")
                if pixelList[i][j] == 2:
                    rect.setFill("red")
                    rect.setOutline("red")
                rect.draw(win)
    #color seed pixel pink
    rect = Rectangle(Point(WIN_W/2,WIN_H/2), Point(WIN_W/2+RENDER_SCALE, WIN_H/2+RENDER_SCALE))
    rect.setFill("HotPink")
    rect.setOutline("HotPink")
    rect.draw(win)


def simulateGrid(grid, xRange, yRange):
    #update locations of all moving particles
    for i in xRange:
        for j in yRange:
            #if grid = 1, there is a wandering particle there - move it
            if grid[i][j] == 1:
                dirX,dirY = chooseDirection()
                if i+dirX < 1 or j+dirY < 1 or i+dirX > len(grid)-2 or j+dirY > len(grid)-2:
                    grid[i][j] = 0
                #only if it is not trying to move into another particle
                if grid[i+dirX][j+dirY] == 0:
                    grid[i+dirX][j+dirY] = grid[i][j]
                    grid[i][j] = 0
            #if the grid point is a stuck particle, check if there are any nonstuck next to it
            if grid[i][j] == 2:
                for dirX,dirY in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    if grid[i+dirX][j+dirY] == 1:
                        grid[i+dirX][j+dirY] = 2


def chooseDirection():
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]
    dirX, dirY = random.choice(directions)
    return dirX, dirY


def progressBar(currentVal, totalVal, bars=20):
    pc = currentVal/totalVal
    numBars = int(math.floor(pc*bars))
    bar = "[" + "\u2588"*numBars + "-"*(bars-numBars) + "]"
    return bar + str(round(pc*100, 2)) + "%"

#######################Main Program#######################

print("Wandering Fractal Version 2.0")
print("By Carter Sifferman, 12/28/2017\n\n")
print("Would you like to input custom parameters? [y/n]")
inp = input("")
while inp != "N" and inp != "n" and inp != "Y" and inp != "y":
    inp = input("Please input 'y' or 'n'")

if inp == "y" or inp == "Y":
    WIN_W = int(input("Output window width [integer]:"))
    WIN_H = int(input("Input window width [integer]:"))
    RENDER_SCALE = int(input("Render Scale [integer]:"))
    ITERATIONS = int(input("Iterations [integer]:"))
    SPACING = int(input("Spacing [integer]:"))
    RENDER_RATIO = int(WIN_W / RENDER_SCALE)

elif inp == "n" or inp == "N":
    input("Press enter to run")

startingGrid = [[0 for i in range(RENDER_RATIO)]for j in range(RENDER_RATIO)]

for i in range(2, len(startingGrid)):
    for j in range(2, len(startingGrid[0])):
        if i % SPACING == 0 and j % SPACING == 0:
            startingGrid[i][j] = 1

startingGrid[int(math.floor(len(startingGrid)/2))][int(math.floor(len(startingGrid)/2))] = 2

forwardXRange = range(1,len(startingGrid)-1)
forwardYRange = range(1,len(startingGrid[0])-1)
backwardXRange = range(len(startingGrid) - 1, 1, -1)
backwardYRange = range(len(startingGrid[0]) - 1, 1, -1)

for i in range(int(math.floor(ITERATIONS/2))):
    simulateGrid(startingGrid, forwardXRange, forwardYRange)
    simulateGrid(startingGrid, backwardXRange, backwardYRange)
    clear()
    print(progressBar(i*2, ITERATIONS))

win = GraphWin("Wandering Fractal V2", WIN_W, WIN_H)

drawGrid(startingGrid)

win.getMouse()
win.close()
