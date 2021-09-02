import CalculatorV3
import solsystem
import plotterV3
import ParticleV3
import data
'''
#EARTH GRAVITY TEST
testing = solsystem.SolarSystem()
testing.addbody('Earth')
testing.addbody('TestBall')
testing.addbody('Sol')
testing.allbodiesadded()
test2 = CalculatorV3.CalculatorV3(1,0.00000000000001)
test2.CromerMethodKECalc()

print(data.TestBall.acceleration - data.Earth.acceleration)


'''
#testing = solsystem.SolarSystem()
#testing.addbody('Sol')
#testing.addbody('Earth')
#testing.addbody('Io')
#testing.addbody('Jupiter')
#testing.addbody('Venus')
#testing.addbody('Ganymede')
#testing.addbody('Saturn')
#testing.addbody('Mercury')
#testing.allbodiesadded()




testing = solsystem.SolarSystem()
testing.addbody('Sol')
testing.addbody('Earth')
testing.addbody('Io')
testing.addbody('Jupiter')
testing.addbody('Venus')
testing.addbody('Ganymede')
testing.addbody('Saturn')
testing.addbody('Mercury')
testing.allbodiesadded()
 #this bit was used in the investigating how timestep messes with plots
test2 = CalculatorV3.CalculatorV3(120000,6000)
test2.CromerMethodKECalc()
test3 = plotterV3.PlotterV3()
test3.CromerorbitPlot()






#used to get long time period graphs for kinetic energy and virial theorem. 
#test2 =CalculatorV3.CalculatorV3(3500000,600)
#test2.EulerMethodKECalc()
#test2.CromerMethodKECalc()
#test2.VirialTheoremCheck()
#test3=plotterV3.PlotterV3()
#test3.CromerorbitPlot()
#test3.VirialPlot()
