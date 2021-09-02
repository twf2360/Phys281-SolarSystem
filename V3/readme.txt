The final code for all this project is in the 'V3' folder, and all other folders have previous version of the code.
Within V3, there are 6 files: data.py, solsystem.py, ParticleV3.py, plotterV3.py, CalculatorV3.py, and testingCode.py

data.py is a list of the names, mass, starting position, starting velocity, and starting acceleration for all the bodies that can currently be modeled by the rest of the code. New bodies can be added to the code by following the conventions shown in the data.py file.

solsystem.py is used to pick which bodies from the data class are to be modeled by the calculator class. If the sun, 'Sol', is not picked, the plots can get quite wierd.

ParticleV3.py is used by the rest of the classes to define a lot of the properties of each of the bodies, and also defines the different methods of updating said properties 

CalculatorV3.py can work out the total system kinetic energy and potential energy for a given timestep between measurements and a total number of said timesteps. This can be used to test the modeled system against the virial theorem. It will also calculate the positions of all of the bodies at all times. It then saves a file of this data, which can be later used or updated.

plotterV3.py reads the saved data  files from the calculators, and then can plot either the orbit positions, the total system kinetic energy with respect to time, and the value of 2T-U with respect to time (Virial Theorem), for some reason, the first plot displayed is alsways in 3D, and so if a 2d plot is needed, two plots must be ran. Tried my best to debug this, but to no avail. Both of the orbit plots are meant to be in 3D 

testingCode.py is a file that i used to write tests for the rest of my solar solar system model. This code however constantly changed as once tests were passed they were discarded for new ones.

Across all files, E and C are often added on to the end or beginning of the names for lists etc, this is to differentiate between whether they are from the Euler method model(E), or the Euler-Cromer method (C)model






