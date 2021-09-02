import math
import numpy as np 
from ParticleV3 import ParticleV3
import copy
import matplotlib.pyplot as plt 
import matplotlib.axes as axs
import data
from mpl_toolkits import mplot3d
import CalculatorV3
import os.path


class PlotterV3:
    '''
    A class that generates various plots to represent the data that is calculated using the CalculatorV3 class. For both the Euler, and Euler-Cromer approximations, there are functions to plot the total kinetic energy, the orbital positions, and the virial thereom. The Virial Theorem Plotter 
    can also be used to compare the two approximations. 
    '''

    def EulerKEplot(self):
        '''
        Plots the total kinetic energy of the system against the time the simulation has been ran through, where the Euler method has been used. requires 
        the Euler method system calculator to have been used first 
        '''
        if not os.path.exists('EulerMethodKE.npy'): #checking the calculator has been ran
            print('No data to plot, please run the Euler Method Kinetic energy calculator function first.')
            raise ValueError('No Data Error')
        eulerplotdata = np.load('EulerMethodKE.npy', allow_pickle = True)
        etimes = []  
        etotalkes = []
       
        for z in range(len(eulerplotdata)):
            etimes.append(eulerplotdata[z][0]) #extracts just the time data and makes the list of that from the big list of all info
            etotalkes.append(eulerplotdata[z][2]) #extracts just the total kinetic energy data and makes a list of just that from the big boi
        
        if (abs(etotalkes[0] - etotalkes[-1])/etotalkes[0]) >= (0.01 * etotalkes[0]) :
            print('Warning: There is a bigger than 1 percent difference between initial and final kinetic energies, showing a problem with the Euler approximation')

            
        plt.plot(etimes, etotalkes, 'red') 
        plt.xlabel('Time')
        plt.ylabel('Kinetic Energy')
        #plt.ylim(bottom =0)
        plt.title('Total Kinetic energy with respect to time, using the Euler Approximation')
        print('The difference between the initial and final kinetic energies after {0} seconds is {1} percent'.format(data.time, ((etotalkes[0]-etotalkes[-1])/etotalkes[0])*100,))
        plt.show()
        
        
            


    def CromerKEplot(self):
        '''
        Plots the total kinetic energy of the system against the time the simulation has been ran through. Requires the Euler-Cromer system calculator to have been 
        ran first
        '''
        if not os.path.exists('CromerMethodKE.npy'): #checking the calculator has been ran
            print('No data to plot, please run the Euler-Cromer Method Kinetic energy calculator function first.')
            raise ValueError('No Data Error')
        cromerplotdata = np.load('CromerMethodKE.npy', allow_pickle = True)
        ctimes = []
        ctotalkes = []
        
        for d in range(len(cromerplotdata)):
            ctimes.append(cromerplotdata[d][0]) # extracts time data from data file
            ctotalkes.append(cromerplotdata[d][2]) #extracts ke data from data file
        
        if (abs(ctotalkes[0] - ctotalkes[-1])/ctotalkes[0]) >= (00.1 * ctotalkes[0]):
            print('Warning: There is a bigger than 1 percent difference between initial and final kinetic energies, showing a problem with the Euler-Cromer approximation')
             
        plt.plot(ctimes, ctotalkes, 'blue') 
        plt.title('Total Kinetic energy with respect to time, using the Euler-Cromer Approximation')
        plt.ylabel('Kinetic Energy')
        plt.xlabel('Time')
        #plt.ylim(bottom =0)
        plt.show()
        print('The difference between the initial and final kinetic energies after {0} seconds is {1} percent'.format(data.time, ((ctotalkes[0]-ctotalkes[-1])/ctotalkes[0])*100,))

    def EulerorbitPlot(self):
        '''
        Plots the orbits of the planets using the Euler approximation, requires the Euler calculator to have been ran first
        '''
        if not os.path.exists('EulerMethodKE.npy'):
            print('No data to plot, please run the Euler Method Kinetic energy calculator function first.')
            raise ValueError('No Data Error')
        eulerdata = np.load('EulerMethodKE.npy', allow_pickle = True)
        
        bodies = [ ]
        for K in range(len(eulerdata)):   
            bodies.append(eulerdata[K][1]) #this will make the bodies list a list of lists, the nestled lists containing the sos list from calculator class at a given time 
         
        bodies = np.array(bodies)
        lob = bodies.transpose() #this turns from [bodies at time 1], [bodies at time 2]etc, to [body 1 at all times], [body 2 at all times,iu]
        xplot =[]
        yplot =[]
        zplot =[]
        for y in range(len(lob)):
            xplotperplanet =[]
            yplotperplanet= []
            zplotperplanet= []
            
            for x in range(len(lob[0])):
                xplotperplanet.append(lob[y][x].position[0])
                yplotperplanet.append(lob[y][x].position[1])
                zplotperplanet.append(lob[y][x].position[2])
            xplot.append(xplotperplanet)
            yplot.append(yplotperplanet)
            zplot.append(zplotperplanet)
        ax = plt.axes(projection = '3d')

        label=[]
        for i in range(len(bodies[0])):
            label.append('{} Orbit'.format(bodies[0][i].Name))
        for i in range(len(bodies[0])):
            ax.plot3D(xplot[i], yplot[i], zplot[i], label = label[i]) 
        plt.legend()
        plt.show()
            
        

            

    def CromerorbitPlot(self):
        '''
        Plots the orbit of the planets using the Euler-Cromer approximation, requires the Euler-Cromer calculator to have been ran first
        ''' 
        if not os.path.exists('CromerMethodKE.npy'):
            print('No data to plot, please run the Euler-Cromer Method Kinetic energy calculator function first.')
            raise ValueError('No Data Error')

        cromerdata = np.load('CromerMethodKE.npy', allow_pickle = True)
        
        bodies = [ ]
        for K in range(len(cromerdata)):   
            bodies.append(cromerdata[K][1]) #this will make the bodies list a list of lists, the nested lists containing the sos list from calculator class at a given time 
         
        bodies = np.array(bodies) #turning list into a np array so the transpose function can be used
        lob = bodies.transpose() #this turns from [bodies at time 1], [bodies at time 2]etc, to [body 1 at all times], [body 2 at all times,iu]
        xplot =[]  
        yplot =[]
        zplot =[]
        for y in range(len(lob)):
            xplotperplanet =[]    
            yplotperplanet= []
            zplotperplanet= []
            
            for x in range(len(lob[0])):
                xplotperplanet.append(lob[y][x].position[0])
                yplotperplanet.append(lob[y][x].position[1])
                zplotperplanet.append(lob[y][x].position[2])
            xplot.append(xplotperplanet)
            yplot.append(yplotperplanet)
            zplot.append(zplotperplanet)
        ax = plt.axes(projection = '3d')

        label=[]
        for i in range(len(bodies[0])):
            label.append('{} Orbit'.format(bodies[0][i].Name))
        for i in range(len(xplot)):
            ax.plot3D(xplot[i], yplot[i], zplot[i], label = label[i]) 
        plt.legend()
        plt.title('Plotting the Orbit of chosen bodies')
        plt.show()
    

    def VirialPlot(self):
        ''' 
        Plots the value of the Virial Theorem against time for any calculators that have been ran. If no Calculators have been ran, will raise a ValueError
        '''

        if os.path.exists('EulerVirial.npy'):
            eulerdata = np.load('EulerVirial.npy', allow_pickle = True)
            datatogettime = np.load('EulerMethodKE.npy', allow_pickle = True)
            timelist = []
            for t in range(len(datatogettime)):
                timelist.append(datatogettime[t][0])
            plt.plot(timelist, eulerdata, 'red', linestyle = '--', label = 'Virial Test for Euler model')
            
                
                
        if os.path.exists('CromerVirial.npy'):
            cromerdata = np.load('CromerVirial.npy', allow_pickle = True)
            datatogettime = np.load('CromerMethodKE.npy', allow_pickle = True)
            timelist =[]
            for t in range(len(datatogettime)):
                timelist.append(datatogettime[t][0])
            plt.plot(timelist, cromerdata, 'blue', linestyle = '--', label = 'Virial Test for Euler-Cromer model')

        if not os.path.exists('CromerVirial.npy'):
            if not os.path.exists('EulerVirial.npy'):
                print('No data for either approximation, please run a calculator first')
                raise ValueError('No Data Error')
           
        plt.legend()
        plt.xlabel('time')
        plt.ylabel('Virial test Value')
        plt.title('Plot showing the values for the Virial test against time.') #The virial test is passed if the value is contant for all times
        #plt.ylim(bottom = 0)
        plt.show()

            

            
        




