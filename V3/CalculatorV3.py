#Class that works out the acceleration of all of the bodies
import math
import numpy as np 
from ParticleV3 import ParticleV3
import copy
import matplotlib.pyplot as plt 
import matplotlib.axes as axs
import solsystem
from mpl_toolkits import mplot3d
import data




totalsystemkeE = [] #empty lists to be later appended by the calculators
totalsystemkeC = []
dataE = [] #data for Euler Method
dataC =[] #data for Cromer Mehod
totalpotentialE = []
totalpotentialC =[]
ax = plt.axes(projection = '3d') #this is how to make 3d graphs
ax.view_init(60, 35) #changes the view of the graph by theta, phi

class CalculatorV3:
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
            for body in solsystem.sos: #iterates through the list for every body
                body.acceleration = np.array([0,0,0], dtype=float)  
                for coa in solsystem.sos: # coa = cause of acceleration - iterates through the list again, as every body is a cause of acceleration. 
                    r = np.linalg.norm(body.position - coa.position) 
                    if body != coa: #the body itself does not cause any acceleration or potential on itself
                        body.acceleration += -(((data.G*coa.mass)/(r**2)) * ((body.position - coa.position)/r))
                        U += -((data.G*coa.mass*body.mass)/(r))  
                
                body.EulerUpdate(self.timestep)  #uses the calulation defined in particle class to update the positions and velocity
                ke += ParticleV3.KineticEnergy(body) 
           
            totalpotentialE.append(U) #appends the empty lists with the calculated values of gravitation potential and kinetic energy
            totalsystemkeE.append(ke)   
            data.time += self.timestep
            
            if x % 100 == 0 : #currently an arbitrary number. MAY NEED TO BE CHANGED
                item = [data.time, copy.deepcopy(solsystem.sos), copy.deepcopy(totalsystemkeE[x]), copy.deepcopy(totalpotentialE[x])] #this is a list of the current time, the current state of the planets, and the total ke of the system at that point in time (x times timestep)
                dataE.append(item)
         
        np.save("EulerMethodKE", dataE, allow_pickle= True) # saves the data to a file so it can later read in

        

    def CromerMethodKECalc(self):
        '''
        uses the Euler-Cromer approximation to model the solar system. This then saves a file called CromerMethodKE.npy, which is the values for all of the data points for the time, all of the data defined in the particle class, and the total system kinetic energy
        '''
        data.time = 0 #sets the time back to 0 so that the process can be compared easier to the Euler method in the Virial Check. Would also like to reset the planets to their initial positions but not sure how
        for y in range(self.iterations): # so the process is repeated through as many iterations as is defined when the class is called
            ke = 0 
            U = 0
            for body in solsystem.sos: #iterates through the list for every body
                body.acceleration = np.array([0,0,0], dtype=float)   
                for coa in solsystem.sos: # coa = cause of acceleration - iterates through the list again, as every body is a cause of acceleration. 
                    r = np.linalg.norm(body.position - coa.position) 
                  
                    if body != coa: #the body itself does not cause any acceleration or potential on itself
                        body.acceleration += -(((data.G*coa.mass)/(r**2)) * ((body.position - coa.position)/r))
                        U +=  -((data.G*coa.mass*body.mass)/(r))
                
                body.CromerUpdate(self.timestep)    #updates position and velocity using the cromer update function defined in the particle class 
                ke += ParticleV3.KineticEnergy(body)
            
            totalsystemkeC.append(ke) #appends the empty lifts defined at the top of the file with data calculated for kinetic energy and potential energy
            totalpotentialC.append(U)

            data.time += self.timestep
            if y % 100 == 0: # currently an arbitrary number. MAY NEED TO BE CHANGED
                item = [data.time, copy.deepcopy(solsystem.sos), copy.deepcopy(totalsystemkeC[y]), copy.deepcopy(totalpotentialC[y])] #this is a list of the current time, the current state of the planets, the total ke of the system at that point in time (x times timestep) and the total potential energy of the system at that time
                dataC.append(item)
        np.save("CromerMethodKE", dataC, allow_pickle=True) #saves the data to a file so that it can later be read


    
    def VirialTheoremCheck(self):
        '''
        Checks either of the approximations models against the virial thereom (that 2T-U should remain constant). The values for each approximation are saved in files called 'EulerVirial.npy' and 'CromerVirial.npy' respectively
        '''
        
        if totalsystemkeE: #will return true if the Euler calculator has been ran, as if it has been run this list will have values in it.
            
            print("Euler Method was used to model the movements of Bodies. Checking this against the Virial Theorem")
            virialdatakeE = [] #empty list to be appeneded - will be full of Kinetic energy data, to be used in the virial theorem, for the Euler model
            virialdatapE = []
            for i in range(len(dataE)):
                virialdatakeE.append(dataE[i][2]) #appends the ke list with kinetic energy data, and the p list with potential energy data
                virialdatapE.append(dataE[i][3])
            T2e = [i * 2 for i in virialdatakeE]
            virialtestE = np.array(T2e) - np.array(virialdatapE)
            percentdiff = (abs(virialtestE[0] - virialtestE[-1])/virialtestE[0]) * 100 #calculates the percentage difference between the final value and the initial.
            np.save('EulerVirial.npy', virialtestE, allow_pickle= True)
            print('This test used the Euler method to model the movement of bodies. The virial test should give a constant value for all times. The percentage difference in the value of the virial test for the first and last entry is {}'.format(percentdiff))

            
        if totalsystemkeC: #will return true if the Euler-Cromer calculator has been ran, as if it has been run this list will have values in it.
            print("Euler-Cromer Method was used to model the movements of Bodies. Checking this against the Virial Theorem")
            virialdatakeC = []
            virialdatapC = []
            for i in range(len(dataC)):
                virialdatakeC.append(dataC[i][2]) #appends the ke list with kinetic energy data, and the p list with potential energy data
                virialdatapC.append(dataC[i][3])
            T2c = [i *2 for i in virialdatakeC]
            virialtestC = np.array(T2c) - np.array(virialdatapC)
            percentdiff = (abs(virialtestC[0] - virialtestC[-1])/virialtestC[0]) * 100
        
            np.save('CromerVirial.npy', virialtestC, allow_pickle= True)
            print('This test used the Euler-Cromer method to model the movement of bodies. The virial test should give a constant value for all times. The difference in the value of the virial test for the first and last entry is {}'.format(percentdiff))

        if not totalsystemkeE: #if this list is empty this if not will continue. This will be the case if the Euler calculator has not been ran
            if not totalsystemkeC:#if this list is empty this if not will continue. This will be the case if the Euler-Cromer calculator has not been ran
                print("Please run a Kinetic energy calculator, either Euler or Euler-Cromer method, in order to test these against the Virial Theorem")
                raise ValueError('No data to test against Virial Theorem')



  





