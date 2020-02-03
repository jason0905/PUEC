import pygame, sys
from pygame.locals import *
from satellite import *

#Getting Config from "config.txt" file
mFile = open("config.txt", 'r')
windowWidth = int(mFile.readline().rstrip().split(' ')[1])
windowHeight = int(mFile.readline().rstrip().split(' ')[1])
FPS = int(mFile.readline().rstrip().split(' ')[1])
numSatellites = int(mFile.readline().rstrip().split(' ')[1])
satelliteList = []
for i in range(numSatellites):
    mFile.readline()
    mFile.readline()
    mass = float(mFile.readline().rstrip().split(' ')[1])
    x = int(mFile.readline().rstrip().split(' ')[1])
    y = int(mFile.readline().rstrip().split(' ')[1])
    xVel = float(mFile.readline().rstrip().split(' ')[1])
    yVel = float(mFile.readline().rstrip().split(' ')[1])
    color = mFile.readline().rstrip().split(' ')[1]
    satelliteList.append(satellite(mass, x, y, xVel, yVel, color))

mForceManager = forceManager(numSatellites, satelliteList)

#COLORS            R    G    B
color_white =   (255, 255, 255)
color_red =     (255,   0,   0)
color_black =   (  0,   0,   0)
color_blue =    (  0,   0, 255)

pygame.init()
mDisplay = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Planet Sim")
mClock = pygame.time.Clock()

#main loop
while True:
    mDisplay.fill(color_white)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    mForceManager.update()
    for i in range(numSatellites):
        satellite = satelliteList[i]
        acceleration = mForceManager.accelerationMatrix[i]
        satellite.update(mDisplay, acceleration, 1)

    pygame.display.update()
    mClock.tick(FPS)
