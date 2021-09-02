import numpy as np
from Particle import Particle
import math
import copy

G=6.67408E-11
earthMass = 5.97237e24   # https://en.wikipedia.org/wiki/Earth
earthRadius = 63710*1e3  # https://en.wikipedia.org/wiki/Earth
Earth = Particle(np.array([0,0,0]), np.array([0,10,0]), np.array([0,0,0]),'Earth', earthMass)
satPosition = earthRadius+(35786*1e3)
satVelocity = math.sqrt(Particle.G*Earth.mass/(satPosition))
Satellite = Particle([satPosition,0,0], [0,satVelocity,0], np.array([0,0,0]), "Satellite", 100.)
satMass = 100.
delta = 6
time = 0
Data = []

for i in range(200000):
    r = np.linalg.norm(Satellite.position - Earth.position)
    Earth.acceleration = -((G*satMass)/(r**2)) * (Earth.position - Satellite.position)/(np.linalg.norm(Earth.position - Satellite.position))# some code here 
    Satellite.acceleration = -((G*earthMass)/(r**2))  * (Satellite.position - Earth.position)/r # some code here 
    Earth.update(delta)
    Satellite.update(delta)
    time += delta
    if i % 100 == 0:
        item = [time, copy.deepcopy(Earth), copy.deepcopy(Satellite)]
        Data.append(item)
        
          
np.save("TwoBodyTest", Data, allow_pickle=True)
