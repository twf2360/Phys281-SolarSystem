import math
import numpy as np 
import copy 
import data
sos = []

class SolarSystem:
    '''
    A class which defines the solar system - adds bodies to a list that is then used by the calculator and plotter classes to use. Only bodies for which there is data in thate data file can be added. 
    If the sun, 'Sol' is not added to the list, the resulting plots can be quite weird.
    '''
    def __init__(self):
        self.solsys = []

    def addbody(self, body):
        ''' 
        A function that takes in the name of a body (in ''), and if data for that body is in the data file, it will add the body to the list of bodies 'currently active' in the solar system
        '''
        if not body in data.lon: 
            print('Body data is not availible, please add to list of planets.')
            raise ValueError('No data error')
        else:
             self.solsys.append(body)

    

    def allbodiesadded(self):
        ''' run this code when all of the bodies have been added using the addbody function '''
        
        for planet in self.solsys:
            for i in range(len( data.lop)):
                if planet == data.lop[i].Name:
                    sos.append(data.lop[i])

        
        
