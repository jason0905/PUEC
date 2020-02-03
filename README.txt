----INSTRUCTIONS----
You will need to install the pygame package, you can easily do this by opening the command prompt and executing
the command: pip install pygame
The program can take infinite (given enough resources) satellites
new satellites and other parameters can be changed in the config file
follow the format in the config file exactly (including line spacing!) when adding new satellites
Each pixel represents one meter
mass is in kilograms
the timestep is currently 1s but can be adjusted to anything in the method call for the satellites update function
for coordinates:
- (0,0) the origin is at the top left corner
- negative x-velocity will result in leftward motion
- negative y-velocity will result in rightward motion

CIRCULAR ORBIT VELOCITY, RADIUS = 200m: 0.4085