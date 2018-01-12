from PIL import Image
import random
import math

SIM_SIZE = 128
SCALE = 4
ITERATIONS = 400
SPACING = 2
WANDER_COLOR = (0,0,0)
STUCK_COLOR = (255,0,0)


#Simulates a given grid by moving all particles, checking for collisions, and trimming those that have wandered off the edge
def simulateGrid(grid, range, edges):
    #update locations of all moving particles
    for i in range:
        for j in range:
            #if grid = 1, there is a wandering particle there - move it
            if grid[i][j] == 1 :
                dirX,dirY = random.choice([(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)])
                #only if it is not trying to move into another particle
                if grid[i+dirX][j+dirY] == 0:
                    grid[i+dirX][j+dirY] = grid[i][j]
                    grid[i][j] = 0
            #if the grid point is a stuck particle, check if there are any nonstuck next to it
            elif grid[i][j] == 2:
                for dirX,dirY in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    if grid[i+dirX][j+dirY] == 1:
                        grid[i+dirX][j+dirY] = 2
    #trim the edges
    for x,y in edges:
        grid[x][y] = 0
        grid[y][x] = 0

#######################Main Program#######################

print("DLA Simulation Version 2.1")
print("By Carter Sifferman, 1/10/2018\n\n")
print("Would you like to input custom parameters? [y/n]")
inp = input("")
while inp != "N" and inp != "n" and inp != "Y" and inp != "y":
    inp = input("Please input 'y' or 'n'")

if inp == "y" or inp == "Y":
    SIM_SIZE = int(input("Simulation Size [integer]:"))
    SCALE = int(input("Render Scale [integer]:"))
    ITERATIONS = int(input("Iterations [integer]:"))

elif inp == "n" or inp == "N":
    input("Press enter to run")

#Create blank starting grid
grid = [[0 for i in range(SIM_SIZE)] for j in range(SIM_SIZE)]

#Fill in starting particles
for i in range(2, len(grid)):
    for j in range(2, len(grid[0])):
        if i % SPACING == 0 and j % SPACING == 0:
            grid[i][j] = 1

#Set center to a "stuck" particle
grid[int(math.floor(len(grid) / 2))][int(math.floor(len(grid) / 2))] = 2

#These ranges are necessary to remove bias caused by checking in the same direction first every time
forwardRange = range(1, len(grid) - 1)
backwardRange = range(len(grid) - 1, 1, -1)

#Define the edges to be trimmed each iteration
edges = list()
for n in range(SIM_SIZE):
    edges.append((0,n))
    edges.append((SIM_SIZE-1,n))

#Simulate the grid for the number of iterations
for i in range(int(math.floor(ITERATIONS/2))):
    simulateGrid(grid, forwardRange, edges)
    simulateGrid(grid, backwardRange, edges)
    print(str(int(i/ITERATIONS*200)) + '%')

#Draw the final grid
img = Image.new('RGB', (len(grid), len(grid[0])), (255, 255, 255))
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            img.putpixel((i, j), (0, 0, 0))
        elif grid[i][j] == 2:
            img.putpixel((i, j), (255, 0, 0))
img = img.resize((SIM_SIZE * SCALE, SIM_SIZE * SCALE))
img.show()