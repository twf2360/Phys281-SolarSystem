import math
import numpy as np 
from Particle import Particle
import copy
import matplotlib.pyplot as plt
import dataclass
import accelerationClass

pllist = accelerationClass.sos
EarthKEplot =[]
SolKEplot=[]
VenusKEplot=[]
JupiterKEplot =[]
GanyKEplot =[]
PlutoKEplot = []
IoKEplot = []
SaturnKEplot = []
MercuryKEplot =[]

timer=[]
'''
class plot:
    def __init__(self, loops = 2000, deltaT=200):
        self.loops = loops
        self.deltaT = deltaT
    
    def __repr__(self):
        return 'testing testing 1,2,3, is this mic even on?'
    
    def KEplot(self):
            
        for y in range(self.loops):
            for planet in pllist:
               ke = Particle.KineticEnergy(planet)
               timer.append(dataclass.time)

               if planet == dataclass.Earth:
                   EarthKEplot.append(ke)
               elif planet == dataclass.Ganymede:
                    GanyKEplot.append(ke)
               elif planet == dataclass.Sol:
                    SolKEplot.append(ke)
               elif  planet == dataclass.Venus:
                    VenusKEplot.append(ke)
               elif planet == dataclass.Io:
                    IoKEplot.append(ke)
               elif planet == dataclass.Jupiter:
                    JupiterKEplot.append(ke)
               elif planet == dataclass.Saturn:
                    SaturnKEplot.append(ke)
               elif planet == dataclass.Mercury:
                    MercuryKEplot.append(ke)
               elif planet == dataclass.Pluto:
                    PlutoKEplot.append(ke)

        plt.plot(SolKEplot, timer, 'green' , label ='Sun KE')
        plt.plot(MercuryKEplot, timer, 'pink' , label ='Mercury KE')
        plt.plot(EarthKEplot, timer, 'blue' , label ='Earth KE')
        plt.plot(JupiterKEplot, timer, 'red' , label ='Jupiter KE')
        plt.plot(VenusKEplot, timer, 'black' , label ='Venus KE')
        plt.plot(GanyKEplot, timer, 'grey' , label ='Ganymede KE')
        plt.plot(PlutoKEplot, timer, 'purple' , label ='Pluto KE')
        plt.plot(IoKEplot, timer, 'yellow' , label ='Io KE')
        plt.plot(SaturnKEplot, timer, 'orange' , label ='Saturn KE')
        plt.legend(loc = 'upper right')
        plt.show()

        

        


                


    #needs fixing - problem for future me    - eventual outcome should a straight line graph showing kinetic energy doesn't change with time, or if it does then that is something to write about in the report.       

test2 = plot(70000, 2000)
plot.KEplot(test2)
'''

# WORKING BY 26 -11 - 19