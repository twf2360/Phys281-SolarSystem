#Class that works out the acceleration of all of the bodies
import math
import numpy as np 
from Particle import Particle
import copy
import matplotlib.pyplot as plt 
import matplotlib.axes as axs
import dataclass
from mpl_toolkits import mplot3d
import plotter



#Defining the current 'state of the solar system'
sos = [dataclass.Sol,dataclass.Earth, dataclass.Jupiter, dataclass.Ganymede, dataclass.Pluto, dataclass.Venus, dataclass.Io, dataclass.Mercury, dataclass.Saturn]
xplot = []
yplot = []
zplot = []

xJUP =[]
yJUP=[]
zJUP =[]

xSO=[]
ySO=[]
zSO=[]

xGany =[]
yGany =[]
zGany = []
xPL = []
yPL =[]
zPL=[]

xVEN = []
yVEN =[]
zVEN =[]
xIO =[]
yIO =[]
zIO =[] 

xMer =[]
yMer =[]
zMer=[]

xSat = []
ySat=[]
zSat=[]

ax = plt.axes(projection = '3d') #this is how to make 3d graphs
ax.view_init(60, 35) #changes the view of the graph by theta, phi
#class that will work out all of the accelerations
class acceleration:
    def __init__(self, iterations=200, timestep=6): #when calling the acceleration class, the number of iterations and the timestep must be defined
        self.iterations = iterations
        self.timestep = timestep

    def accelCalc(self):
        
        for x in range(self.iterations): # so the process is repeated through as many iterations as is defined when the class is called
            for body in sos: #iterates through the list for every body
                body.acceleration = np.array([0,0,0], dtype=float)   
                for coa in sos: # coa = cause of acceleration - iterates through the list again, as every body is a cause of acceleration. 
                    r = np.linalg.norm(body.position - coa.position) 
                    if body != coa: #the body itself does not cause any acceleration on itself
                        body.acceleration += -(((dataclass.G*coa.mass)/(r**2)) * ((body.position - coa.position)/r))
                body.update(self.timestep)        

                            
                
                
            dataclass.time += self.timestep
            
            #PLOTTING TO TEST
            xplot.append(dataclass.Earth.position[0])
            yplot.append(dataclass.Earth.position[1])        
            zplot.append(dataclass.Earth.position[2]) 
            xJUP.append(dataclass.Jupiter.position[0])
            yJUP.append(dataclass.Jupiter.position[1])
            zJUP.append(dataclass.Jupiter.position[2])
            xSO.append(dataclass.Sol.position[0])
            ySO.append(dataclass.Sol.position[1])
            zSO.append(dataclass.Sol.position[2])
            xGany.append(dataclass.Ganymede.position[0])
            yGany.append(dataclass.Ganymede.position[1])
            zGany.append(dataclass.Ganymede.position[2])
            xPL.append(dataclass.Pluto.position[0])
            yPL.append(dataclass.Pluto.position[1])
            zPL.append(dataclass.Pluto.position[2])
            xVEN.append(dataclass.Venus.position[0])
            yVEN.append(dataclass.Venus.position[1])
            zVEN.append(dataclass.Venus.position[2])
            xIO.append(dataclass.Io.position[0])
            yIO.append(dataclass.Io.position[1])
            zIO.append(dataclass.Io.position[2])
            xMer.append(dataclass.Mercury.position[0])
            yMer.append(dataclass.Mercury.position[1])
            zMer.append(dataclass.Mercury.position[2])
            xSat.append(dataclass.Saturn.position[0])
            ySat.append(dataclass.Saturn.position[1])
            zSat.append(dataclass.Saturn.position[2]) 

        
        ax.plot3D(xJUP,yJUP,zJUP, 'red', label = 'Jupiter Orbit')      
        ax.plot3D(xplot,yplot, zplot, 'green', label = 'Earth Orbit') 
        ax.plot(xSO,ySO,zSO, 'blue', label = 'Sun Orbit')
        ax.plot(xGany, yGany, zGany, 'grey', label = 'Ganymede  Orbit')
        ax.plot(xVEN,yVEN,zVEN, 'black', label = 'Venus Orbit')
        ax.plot(xIO,yIO,zIO, 'yellow', label = 'Io Orbit')
        #ax.plot(xPL, yPL, zPL, 'purple', label = 'Pluto')
        ax.plot(xMer, yMer, zMer, 'pink', label = 'Mercury Orbit')
        ax.plot(xSat, ySat, zSat, 'purple', label = 'Saturn Orbit')
        plt.legend(loc = 'upper right')
        plt.show()
        
                        
    def __repr__(self):
        return 'Final positions of {0},{1},{2} are {3},{4},{5}'.format(dataclass.Sol.Name, dataclass.Jupiter.Name, dataclass.Earth.Name, dataclass.Sol.position, dataclass.Jupiter.position, dataclass.Earth.position)

                
#ideas - add axis labels in au, add labels for each of the lines, etc 26-11-19 work! 
# ADD AN ERROR CHECKER - TOTAL KE CHECKER??
# Add a way of using a different algorithm - e.g. EUler cromer 
# save some of the outputs into a file 
# once e-mag is done, lets just fucking grind this boi. 
# try and make this more general, but this is a good starting point. 
# euler vs euler cromer
#angular momentum 
# percentage or fractional change is often better
# just read the lectures you plebian
test = acceleration(50000, 2000)
acceleration.accelCalc(test)
#print(test)
print(dataclass.time)

#print(xplot)


