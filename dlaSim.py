import pyglet
from pyglet.gl import *
import random
import math

TIME_STEP = 1 / 30
WANDER_COLOR = (255, 255, 255)
STUCK_COLOR = (255, 0, 0)
SIM_SIZE = 256
SCALE = 4
SPACING = 2

class Environment:
    COLLISION_DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    MOVEMENT_DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]

    def __init__(self):
        #create empty grid
        self.grid = [[0 for i in range(SIM_SIZE)] for j in range(SIM_SIZE)]
        # Fill in starting particles
        for i in range(2, len(self.grid)):
            for j in range(2, len(self.grid[0])):
                if i % SPACING == 0 and j % SPACING == 0:
                    self.grid[i][j] = 1
        # Set center to a "stuck" particle
        self.grid[int(math.floor(len(self.grid) / 2))][int(math.floor(len(self.grid) / 2))] = 2
        # Define the edges to be trimmed each iteration
        self.edges = list()
        for n in range(SIM_SIZE):
            self.edges.append((0, n))
            self.edges.append((SIM_SIZE - 1, n))

    #Simulates a given grid by moving all particles, checking for collisions, and trimming those that have wandered off the edge
    def simulate(self, deltaTime):
        #update locations of all moving particles
        #'ranges' is used to go through the particles in both directions, eliminating bias
        ranges = [range(1, len(self.grid) - 1), range(len(self.grid)-2, 1, -1)]
        for xRange in ranges:
            for i in xRange:
                for j in xRange:
                    #if grid = 1, there is a wandering particle there - move it
                    if self.grid[i][j] == 1 :
                        dirX,dirY = random.choice(self.MOVEMENT_DIRECTIONS)
                        #only if it is not trying to move into another particle
                        if self.grid[i+dirX][j+dirY] == 0:
                            self.grid[i+dirX][j+dirY] = self.grid[i][j]
                            self.grid[i][j] = 0
                    #if the grid point is a stuck particle, check if there are any nonstuck next to it
                    elif self.grid[i][j] == 2:
                        for dirX,dirY in self.COLLISION_DIRECTIONS:
                            if self.grid[i+dirX][j+dirY] == 1:
                                self.grid[i+dirX][j+dirY] = 2
        #trim the edges
        for x,y in self.edges:
            self.grid[x][y] = 0
            self.grid[y][x] = 0

    def render(self):
        #convert grid to 1d list
        l1 = []
        l2 = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[i][j] == 1:
                    l1.append(i)
                    l1.append(j)
                if self.grid[i][j] == 2:
                    l2.append(i)
                    l2.append(j)
        wandering = tuple(l1)
        stuck = tuple(l2)
        glPointSize(float(SCALE))
        glColor3f(*WANDER_COLOR)
        pyglet.graphics.draw(int(len(l1)/2), pyglet.gl.GL_POINTS,
                             ('v2i',wandering))
        glColor3f(*STUCK_COLOR)
        pyglet.graphics.draw(int(len(l2)/2), pyglet.gl.GL_POINTS,
                             ('v2i',stuck))


#######################Main Program#######################
def main():
    env = Environment()
    window = pyglet.window.Window(SIM_SIZE * SCALE, SIM_SIZE * SCALE)
    glScalef(SCALE, SCALE, SCALE)
    pyglet.clock.schedule_interval(env.simulate, TIME_STEP)

    # draw to window
    @window.event
    def on_draw():
        window.clear()
        env.render()

    pyglet.app.run()

if __name__ == '__main__':
    main()
