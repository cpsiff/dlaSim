# DLA Simulation
Simple diffusion limited aggregation simulation written in Python. Displays a graphics window to the user with the specified window size, scale, and iterations.
## Example Output
<p align="center">
  <img src="https://i.imgur.com/gnBThAU.png"></img>
</p>

## How It Works
The program works by simulating each particle simultaneously. The starting particles are spaced according to the user's specifications (default every other pixel). Each particle does a "drunkard's walk" - randomly choosing to move up, down, left, right, or stay in place. If a particle sticks to a "stuck" particle, it becomes stuck itself, and stops wandering. Upon initialization there is only one "stuck" particle in the center of the plane. 

## Dependencies and How to Install Them
The only dependency is <a href = "https://pillow.readthedocs.io/en/5.0.0/"> Pillow </a>, a fork of PIL. This library makes it easy to draw graphics objects and output images. Installation for the library can be found on Pillow's website.
