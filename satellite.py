import pygame
from pygame.locals import *


#COLORS            R    G    B
color_white =   (255, 255, 255)
color_red =     (255,   0,   0)
color_black =   (  0,   0,   0)
color_blue =    (  0,   0, 255)

ID = 0

class satellite():
    
    def __init__(self, mass, x, y, x_vel, y_vel, color = "color_black"):
        global ID
        self.ID = ID
        ID += 1
        self.mass = mass
        self.x = x
        self.y = y
        self.xVel = x_vel
        self.yVel = y_vel
        self.color = color

    def update(self, display, acceleration, timestep):
        self.x += self.xVel * timestep + 0.5*acceleration[0]*(timestep)**2
        self.y += self.yVel * timestep + 0.5*acceleration[1]*(timestep)**2
        self.xVel += acceleration[0]*timestep
        self.yVel += acceleration[1]*timestep
        #print("Planet %d: " %(self.ID), self.xVel, self.yVel)
        '''if(self.ID == 1):
            print("X: ", self.xVel, "Y: ", self.yVel)'''
        pygame.draw.circle(display, eval(self.color), (int(self.x), int(self.y)), 5, 2) 

class forceManager():
    
    
    def __init__(self, numSatellites, satelliteList):
        self.numSatellites = numSatellites
        self.satelliteList = satelliteList
        self.forceMatrix = []
        self.accelerationMatrix = []
        for i in range(numSatellites):
            self.forceMatrix.append([[0,0]]*numSatellites)
            self.accelerationMatrix.append([0,0])

    def update(self):
        G = 6.67408 * (10**-11) #meters^3 kg^-1 s^-2
        for x in range(self.numSatellites):
            for y in range(self.numSatellites):
                #print("doing %d %d" %(x,y))
                sat1 = self.satelliteList[x]
                sat2 = self.satelliteList[y]
                distance = ((sat1.x - sat2.x)**2 + (sat1.y - sat2.y)**2)**0.5
                #print(distance)
                if distance == 0:
                    if(sat1.ID != sat2.ID):
                        print("zero distance!")
                    self.forceMatrix[x][y] = [0,0]
                    continue
                force = G * sat1.mass * sat2.mass / (distance**3)
                self.forceMatrix[x][y] = [force * (sat2.x - sat1.x), force * (sat2.y - sat1.y)]
        self.generateAcceleration()

    def generateAcceleration(self):
        #print("running")
        for row in range(self.numSatellites):
            mRow = self.forceMatrix[row]
            xAccel, yAccel = 0,0
            for force in mRow:
                xAccel += force[0]
                yAccel += force[1]

            xAccel = xAccel / self.satelliteList[row].mass
            yAccel = yAccel / self.satelliteList[row].mass
            self.accelerationMatrix[row] = [xAccel,yAccel]
    
                
                
                
                
    

    
        
