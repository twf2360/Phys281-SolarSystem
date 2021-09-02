import math
import numpy as np 
from ParticleV2 import ParticleV2
import copy
import matplotlib.pyplot as plt 
import matplotlib.axes as axs
import dataclassV2
from mpl_toolkits import mplot3d


class PlotterV2:
    #def __init__ (self):

    def __repr__(self):
        return 'testing testing 123, is this mic even on?'
    
    def EulerKEplot(self):
        '''
        a function that plots the total kinetic energy of the system against the time the simulation has been ran through, where the Euler method has been used. requires 
        the Euler method system calculator to have been used first 
        '''
        eulerplotdata = np.load('EulerMethodKE.npy', allow_pickle = True)
        etimes = []  
        etotalkes = []
        if not eulerplotdata.all: #this will go through if the list is empty 
            print('No data to plot, please run the Euler Method Kinetic energy calculator function first.')
            raise ValueError('No Data Error')
        for z in range(len(eulerplotdata)):
            etimes.append(eulerplotdata[z][0]) #extracts just the time data and makes the list of that from the big list of all info
            etotalkes.append(eulerplotdata[z][2]) #extracts just the total kinetic energy data and makes a list of just that from the big boi
        
        if abs(etotalkes[0] - etotalkes[-1]) >= (0.01 * etotalkes[0]) :
            print('Warning: There is a bigger than 1 percent difference between initial and final kinetic energies, showing a problem with the Euler approximation')

            
        plt.plot(etimes, etotalkes, 'red', linestyle = '--') #add title 'Total kinetic energy of the system with respect to time, using'
        plt.xlabel('Time')
        plt.ylabel('Kinetic Energy')
        plt.ylim(bottom =0)
        plt.text(1,1, 'The difference between the initial and final kinetic energies after {0} seconds is {1} percent'.format(dataclassV2.time, (etotalkes[0]/etotalkes[-1])*100,))
        plt.show()
        
        
            


    def CromerKEplot(self):
        '''
        a function that plots the total kinetic energy of the system against the time the simulation has been ran through. Requires the Euler Cromer system calculator to have been 
        ran first
        '''
        cromerplotdata = np.load('CromerMethodKE.npy', allow_pickle = True)
        ctimes = []
        ctotalkes = []
        if not cromerplotdata.all: #will go through if the list is empty
            print('No data to plot, please run the Euler-Cromer Method Kinetic energy calculator function first.')
            raise ValueError('No Data Error')
        for d in range(len(cromerplotdata)):
            ctimes.append(cromerplotdata[d][0]) # extracts time data from data file
            ctotalkes.append(cromerplotdata[d][2]) #extracts ke data from data file
        
        if abs(ctotalkes[0] - ctotalkes[-1]) >= (00.1 * ctotalkes[0]):
            print('Warning: There is a bigger than 1 percent difference between initial and final kinetic energies, showing a problem with the Euler-Cromer approximation')
             
        plt.plot(ctimes, ctotalkes, 'blue') #add title, something like 'Total kinetic energy of the system with respect to time, using'
        plt.xlabel('Time')
        plt.ylabel('Kinetic Energy')
        plt.ylim(bottom =0)
        plt.show()

    def EulerorbitPlot(self):
        '''
        a function that plots the orbits of the planets using the euler approximation
        '''
        
        eulerdata = np.load('EulerMethodKE.npy', allow_pickle = True)
        if not eulerdata.any:
            print('No data to plot, please run the Euler Method Kinetic energy calculator function first.')
            raise ValueError('No Data Error')
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
        for i in range(len(xplot)):
            ax.plot3D(xplot[i], yplot[i], zplot[i], label = label[i]) 
        plt.legend()
        plt.show()
            
        

            

    def CromerorbitPlot(self):
        '''
        a function that plots the orbit of the planets using the cromer approximation
        ''' 
        

        cromerdata = np.load('CromerMethodKE.npy', allow_pickle = True)
        if not cromerdata.any:
            print('No data to plot, please run the Euler-Cromer Method Kinetic energy calculator function first.')
            raise ValueError('No Data Error')

        bodies = [ ]
        for K in range(len(cromerdata)):   
            bodies.append(cromerdata[K][1]) #this will make the bodies list a list of lists, the nestled lists containing the sos list from calculator class at a given time 
         
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
        for i in range(len(xplot)):
            ax.plot3D(xplot[i], yplot[i], zplot[i], label = label[i]) 
        plt.legend()
        plt.show()
    

    def VirialPlot(self):
            cromerdata = np.load('CromerVirial.npy', allow_pickle = True)
            eulerdata = np.load('EulerVirial.npy', allow_pickle = True)
            datatogettime = np.load('CromerMethodKE', allow_pickle = True)
            timelist = []
            for t in range(len(datatogettime)):
                timelist.append(datatogettime[t][0])
            if not cromerdata and eulerdata:
                print('No data for either approximation, please run a calculator first')

            plt.plot(timelist, cromerdata, 'blue', linestyle = '--', label = 'Virial Test for Euler-Cromer model')
            plt.plot(timelist, eulerdata, 'red', linestyle = '--', label = 'Virial Test for Euler-Cromer model')
            plt.legend()
            plt.title('Plot showing the values for the Virial test against time. The virial test is passed if the value is contant for all times')
            plt.show()

            
            
            
        



testing = PlotterV2()


PlotterV2.CromerorbitPlot(testing)

