"""
Advection Equation

@author: Manuel Bolduc

Feb 28th 2020
"""
import numpy as np
from matplotlib import pyplot as plt 

#We are working on the interval [0,1]
x=np.linspace(0,1,1000)

#We use dx as the spacing between the points on [0,1]
dx=np.abs(x[0]-x[-1])/len(x)

#We take dt=2*dx so that the Lax friedrichs scheme is stable
dt=2*dx

#initialize f1 and f2 (f1 is f for FTCS, f2 is f for Lax Friedrichs)
f1=np.zeros([len(x)])
f1[:]=x[:] #initial conditions
f2=f1
#We use u=-0.1
u=-0.1

for i in range(1000):

	## FTCS ##
	f1=f1-u*dt/(2*dx)*(np.roll(f1,-1)-np.roll(f1,1))#Update step

	#Fixed BC
	f1[0]=x[0]
	f1[-1]=x[-1]

	## LAX FRIEDRICHS ##
	f2=0.5*(np.roll(f2,-1)+np.roll(f2,1))-u*dt/(2*dx)*(np.roll(f2,-1)-np.roll(f2,1))#Update Step
	#Fixed BC
	f2[0]=x[0]
	f2[-1]=x[-1]

	#Animation
	if i%10==0:
		plt.clf()
		plt.subplot(121)
		plt.title('FTCS')
		plt.plot(x,f1)

		plt.subplot(122)
		plt.title('Lax Friedrichs')
		plt.plot(x,f2)
		plt.show()
		plt.pause(0.05)
