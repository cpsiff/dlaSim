# DLA Simulation
Simple diffusion limited aggregation simulation written in Python. Displays a graphics window to the user with the specified window size, scale, and iterations.
## Example Output
<p align="center">
  <img src="https://i.imgur.com/Amvsxgd.png"></img>
</p>

## How It Works
The program works by simulating each particle simultaneously. The starting particles are spaced according to the user's specifications (default every other pixel). Each particle does a "drunkard's walk" - randomly choosing to move up, down, left, right, or stay in place. If a particle sticks to a "stuck" particle, it becomes stuck itself, and stops wandering. By default there is one "stuck" particle in the center of the plane. 

## Dependencies and How to Install Them
The only dependency is <a href = "http://mcsp.wartburg.edu/zelle/python/graphics.py"> graphics.py </a> by John Zelle. The library makes it easy to draw graphics objects and makes the code much more readable. To install the library, put the graphics.py file anywhere python can see it. If you just want to install it for one project, put it in the same directory as that project. To install it for all projects put it in your python installation's /lib/site-packages folder
