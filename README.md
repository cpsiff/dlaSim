# DLA Simulation
Simple diffusion limited aggregation simulation written in Python. Displays a graphics window to the user with the specified window size, scale, and iterations.
## Example Output
<p align="center">
  <img src="https://i.imgur.com/Amvsxgd.png"></img>
</p>

## How It Works
The program works by simulating each particle simultaneously. The starting particles are spaced according to the user's specifications (default every other pixel). Each particle does a "drunkard's walk" - randomly choosing to move up, down, left, right, or stay in place. If a particle sticks to a "stuck" particle, it becomes stuck itself, and stops wandering. By default there is one "stuck" particle in the center of the plane. 
