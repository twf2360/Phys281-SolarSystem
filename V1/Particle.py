import math
import numpy as np 

class Particle:
    def __init__(self, Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,-10,0], dtype=float), Name='Ball', Mass=1.0):
        self.position = np.array(Position, dtype = float)
        self.velocity = np.array(Velocity, dtype=float)    
        self.acceleration = np.array(Acceleration, dtype = float)
        self.mass = Mass
        self.Name = Name 

    def __repr__(self):
        return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}'.format(self.Name,self.mass,self.position, self.velocity,self.acceleration)

    def update(self, deltaT):
        v = self.velocity
        x = self.position 
        a = self.acceleration
        
        x += v*deltaT
        v += a*deltaT
    G=6.67408E-11
   
    def KineticEnergy(self):
        v = np.linalg.norm(self.velocity)
        m = self.mass 
        return 0.5*m*v**2

