# DLA Simulation
Simple diffusion limited aggregation simulation written in Python. Displays a graphics window to the user with the specified window size, scale, and iterations.
### Difference between versions
The **PIL** version simulates the whole grid and outputs the final output to an image file.

The **Pyglet** version draws the simulation to a window as it is being simulated. It is prettier to look at but more work to get images out of.

## Example Output
<p align="center">
  <img src="https://i.imgur.com/gnBThAU.png"></img>
</p>

## How It Works
The program works by simulating each particle simultaneously. The starting particles are spaced according to the user's specifications (default every other pixel). Each particle does a "drunkard's walk" - randomly choosing to move up, down, left, right, or stay in place. If a particle sticks to a "stuck" particle, it becomes stuck itself, and stops wandering. Upon initialization there is only one "stuck" particle in the center of the plane. 

## Dependencies and How to Install Them
The only dependency for the normal version is <a href = "https://pillow.readthedocs.io/en/5.0.0/"> Pillow </a>, a fork of PIL. This library makes it easy to draw graphics objects and output images. Installation for the library can be found on Pillow's website.

For the "dlaSim_pyglet" version, you will need to install <a href = "https://bitbucket.org/pyglet/pyglet/wiki/Download"> pyglet. </a> Instructions for installation can be found on pyglet's website.
