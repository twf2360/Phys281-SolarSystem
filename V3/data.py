#SOLAR SYSTEM DATA
import math
import numpy as np 
from ParticleV3 import ParticleV3
import copy
import matplotlib as plt 

#For future bodies added to this file, follow the same convention laid out by the already added bodies, and ensure that the names of body is added to the 'lon' list at the bottom, and the body as a whole is added to the 'lob' list. 

#Universal data
G=6.67408E-11
au = 149597870700
time = 0 

#Sun
sunMass = 1988500e24 
sunPosition = np.array([-5.167463430197339e8,1.123866949846899e9,2.026322637655481e6], dtype = float)
sunVel = np.array([-1.461396883032566e1,-2.680383180777907e0,4.008504030050694e-1], dtype=float)
sunAccel = np.array([0,0,0], dtype=float)
Sol = ParticleV3(sunPosition, sunVel, sunAccel , 'Sol', sunMass) 

#Earth
earthMass = 5.97237e24   
earthPosition = np.array([7.760768396289486e10,1.265949225405731e11,-4.283205381728709e6], dtype=float)
earthVel = np.array([-2.578528277071652e4,1.564154835387608e4,-7.434909738091022e-1], dtype = float)
earthAccel = np.array([0,0,0] ,dtype=float)
Earth = ParticleV3(earthPosition, earthVel, earthAccel, 'Earth', earthMass)

#Jupiter
jupMass = 1898.13e24
jupPosition = np.array([3.254621581637136e10,-7.824327097270645e11,2.516842068094909e9], dtype= float)
jupVel = np.array([1.289362153252854e4, 1.165773392952160e3,-2.933343239159653e2], dtype= float)
jupAccel = np.array([0,0,0], dtype=float)
Jupiter = ParticleV3(jupPosition,jupVel, jupAccel, 'Jupiter', jupMass)

#Venus 
venMass = 48.685e23
venPosition = np.array([5.252805747513023e10,-9.390698721013290e10,-4.362990951083869e9], dtype=float)
venVel = np.array([3.033017504712624e4,1.694751058776131e4,-1.518131228571090e3], dtype=float)
venAccel = np.array([0,0,0], dtype=float)
Venus = ParticleV3(venPosition, venVel, venAccel, 'Venus', venMass)



#Ganymede
ganyMass = 1482e20
ganyPosition = np.array([3.311005260224447e10,-7.833404584259014e11,2.490043633446276e9], dtype=float)
ganyVel = np.array([2.214181919831798e4,6.918126426431146e3,4.991723372195311e1], dtype=float)
ganyAccel = np.array([0,0,0], dtype=float)
Ganymede = ParticleV3(ganyPosition, ganyVel, ganyAccel, 'Ganymede', ganyMass)


#Pluto
plMass = 1.307e22
plPosition = np.array([1.922481551595635e12, -4.695026805155170e12, -5.369986975995874e10], dtype=float)
plVel = np.array([5.150578012184086e3, 8.892017921263695e2,-1.606541595082319e3], dtype=float)
plAccel = np.array([0,0,0], dtype=float)
Pluto = ParticleV3(plPosition, plVel, plAccel, 'Pluto', plMass)

#Io
ioMass = 893.3e20
ioPosition = np.array([3.247428388278171e10,-7.828497377873671e11,2.500561850996852e9], dtype=float)
ioVel = np.array([2.990769745586246e4,-1.768308146176956e3,-1.522695187468476e2], dtype=float)
ioAccel = np.array([0,0,0], dtype=float)
Io = ParticleV3(ioPosition, ioVel, ioAccel, 'Io', ioMass)

#Mercury
merMass = 3.302e23
merPosition = np.array([-1.422157328212764e10,4.587135028700352e10,4.915752650177458e9], dtype=float)
merVel = np.array([-5.637147885838698e4,-1.247272264289699e4,4.151335408403708e3], dtype=float)
merAccel = np.array([0,0,0], dtype=float)
Mercury = ParticleV3(merPosition, merVel, merAccel, 'Mercury', merMass)


#Saturn
saturnMass = 5.6834e26
saturnPosition = np.array([5.375742893579234e11,-1.400869277494722e12, 2.957732795421660e9], dtype = float) 
saturnVel = np.array([8.482842743013379e3,3.431245025225380e3,-3.968860925203656e2], dtype = float)
saturnAccel = np.array([0,0,0], dtype = float)
Saturn = ParticleV3(saturnPosition, saturnVel, saturnAccel, 'Saturn', saturnMass)

#testBall
ballMass = 10
ballPosition = np.array([(7.760768396289486e10 + 6371e3) ,1.265949225405731e11,-4.283205381728709e6], dtype = float) #same position as earth for y and z, plus one earth radius for x, used for testing
ballVel = np.array([0,0,0], dtype= float)
ballAccel = np.array([0,0,0], dtype = float)
TestBall = ParticleV3(ballPosition, ballVel,ballAccel, 'TestBall', ballMass)

lop = [Sol, Earth, Jupiter, Venus, Ganymede, Io, Pluto, Saturn, Mercury, TestBall]
lon = [Sol.Name, Earth.Name, Jupiter.Name, Venus.Name, Ganymede.Name, Io.Name, Pluto.Name, Saturn.Name, Mercury.Name, TestBall.Name] #ENSURE NAMES OF ALL BODIES ARE IN HERE IF DATA IS UPDATED
