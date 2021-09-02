#Class that works out the acceleration of all of the bodies
import math
import numpy as np 
from ParticleV2 import ParticleV2
import copy
import matplotlib.pyplot as plt 
import matplotlib.axes as axs
import dataclassV2
from mpl_toolkits import mplot3d
import sympy



#Defining the current 'state of the solar system'
sos = [dataclassV2.Sol,dataclassV2.Earth, dataclassV2.Jupiter, dataclassV2.Ganymede, dataclassV2.Pluto, dataclassV2.Venus, dataclassV2.Io, dataclassV2.Mercury, dataclassV2.Saturn]
totalsystemkeE = []
totalsystemkeC = []
dataE = [] #data for Euler Method
dataC =[] #data for Cromer Mehod
totalpotentialE = []
totalpotentialC =[]
ax = plt.axes(projection = '3d') #this is how to make 3d graphs
ax.view_init(60, 35) #changes the view of the graph by theta, phi

class CalculatorV2:
    '''
    This class is used to model the system defined by the sos list above, using either the Euler or the Euler-Cromer approximations. It will then also calculate the values for the Virial
    theorem for each approximation. 
    '''
    def __init__(self, iterations=200, timestep=6): #when calling the acceleration class, the number of iterations and the timestep must be defined
        self.iterations = iterations
        self.timestep = timestep

    def EulerMethodKECalc(self):
        '''
        uses the Euler approximation to model the solar system. This then saves a file called EulerMethodKE.npy, which is the values for all of the data points for the time, all of the data defined in the particle class, and the total system kinetic energy

        '''
        
        for x in range(self.iterations): # so the process is repeated through as many iterations as is defined when the class is called
            ke = 0
            U = 0 
            for body in sos: #iterates through the list for every body
                body.acceleration = np.array([0,0,0], dtype=float)  
                for coa in sos: # coa = cause of acceleration - iterates through the list again, as every body is a cause of acceleration. 
                    r = np.linalg.norm(body.position - coa.position) 
                    if body != coa: #the body itself does not cause any acceleration on itself
                        body.acceleration += -(((dataclassV2.G*coa.mass)/(r**2)) * ((body.position - coa.position)/r))
                        U += -((dataclassV2.G*coa.mass*body.mass)/(r**2))  #body doesn't cause any potential on itself
                
                body.EulerUpdate(self.timestep)  
                ke += ParticleV2.KineticEnergy(body)
                totalpotentialE.append(U)
            
            totalsystemkeE.append(ke)   
            dataclassV2.time += self.timestep
            
            if x % 100 == 0 : #currently an arbitrary number. MAY NEED TO BE CHANGED
                item = [dataclassV2.time, copy.deepcopy(sos), copy.deepcopy(totalsystemkeE[x])] #this is a list of the current time, the current state of the planets, and the total ke of the system at that point in time (x times timestep)
                dataE.append(item)
         
        np.save("EulerMethodKE", dataE, allow_pickle= True)
        print('lÖÖps are done')
        return totalsystemkeE #this is so it can be used in my Virial Thereom check - not sure if necessary
        

    def CromerMethodKECalc(self):
        '''
uses the Euler-Cromer approximation to model the solar system. This then saves a file called CromerMethodKE.npy, which is the values for all of the data points for the time, all of the data defined in the particle class, and the total system kinetic energy
        '''

        for y in range(self.iterations): # so the process is repeated through as many iterations as is defined when the class is called
            ke = 0 
            U = 0
            for body in sos: #iterates through the list for every body
                body.acceleration = np.array([0,0,0], dtype=float)   
                for coa in sos: # coa = cause of acceleration - iterates through the list again, as every body is a cause of acceleration. 
                    r = np.linalg.norm(body.position - coa.position) 
                    if body != coa: #the body itself does not cause any acceleration on itself
                        body.acceleration += -(((dataclassV2.G*coa.mass)/(r**2)) * ((body.position - coa.position)/r))
                        U +=  -((dataclassV2.G*coa.mass*body.mass)/(r**2))
                
                body.CromerUpdate(self.timestep)     
                ke += ParticleV2.KineticEnergy(body)
            
            totalsystemkeC.append(ke)
            totalpotentialC.append(U)

            dataclassV2.time += self.timestep
            if y % 100 == 0: # currently an arbitrary number. MAY NEED TO BE CHANGED
                item = [dataclassV2.time, copy.deepcopy(sos), copy.deepcopy(totalsystemkeC[y])] #this is a list of the current time, the current state of the planets, and the total ke of the system at that point in time (x times timestep)
                dataC.append(item)
        np.save("CromerMethodKE", dataC, allow_pickle=True)
        print('more loops have been done') # calculation completed?
        return totalsystemkeC  #again, so it can be used in Virial Theorem Checker - not sure if necessary

    
    def VirialTheoremCheck(self):
        '''
        Checks either of the approximations models against the virial thereom (that 2T-U should remain constant). The values for each approximation are saved in files called 'EulerVirial.npy' and 'CromerVirial.npy' respectively
        '''
        
        if self.EulerMethodKECalc() != 0:
            keTotal = self.EulerMethodKECalc()
            print("Euler Method was used to model the movements of Bodies. Checking this against the Virial Theorem")#
            virialtestE = 2*totalsystemkeE - totalpotentialE
            diff = abs(virialtestE[0] - virialtestE[-1])
            np.save('EulerVirial.npy', virialtestE, allow_pickle= True)
            print('This test used the Euler method to model the movement of bodies. The virial test should give a constant value for all times. The difference in the value of the virial test for the first and last entry is {}'.format(diff))

            
        if self.CromerMethodKECalc() !=0:
            keTotal = self.CromerMethodKECalc()
            print("Euler-Cromer Method was used to model the movements of Bodies. Checking this against the Virial Theorem")
            virialtestC = 2*totalsystemkeC - totalpotentialC
            diff = abs(virialtestC[0] - virialtestC[-1])
            np.save('CromerVirial.npy', virialtestC, allow_pickle= True)
            print('This test used the Euler-Cromer method to model the movement of bodies. The virial test should give a constant value for all times. The difference in the value of the virial test for the first and last entry is {}'.format(diff))

        if self.CromerMethodKECalc() and self.EulerMethodKECalc() == 0:
            print("Please run a Kinetic energy calculator, either Euler or Euler-Cromer method, in order to test these against the Virial Theorem")
            raise ValueError('No data to test against Virial Theorem')



        
        
            
           
            
            
                        
    def __repr__(self):
        return 'Final positions of {0},{1},{2} are {3},{4},{5}'.format(dataclassV2.Sol.Name, dataclassV2.Jupiter.Name, dataclassV2.Earth.Name, dataclassV2.Sol.position, dataclassV2.Jupiter.position, dataclassV2.Earth.position)

                
# ideas - add axis labels in au, add labels for each of the lines, etc 26-11-19 work! 
# ADD AN ERROR CHECKER - TOTAL KE CHECKER??

# once e-mag is done, lets just fucking grind this boi. 
# try and make this more general, but this is a good starting point. 
# euler vs euler cromer
# momentum 
# percentage or fractional change is often better
# just read the lectures you plebian

test = CalculatorV2(50000, 2000)
CalculatorV2.EulerMethodKECalc(test)
CalculatorV2.CromerMethodKECalc(test)




