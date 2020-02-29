"""
1-Dimensional Hydro Solver 

@author: Manuel Bolduc
Collaborators: Mathieu Bruneault, Alex Khoury

Feb 28th 2020
"""
import numpy as np
from matplotlib import pyplot as plt

# We solve the equation on [0,1]
x=np.linspace(0,1,1000)

# We define dx as the spacing between the points on [0,1]
dx=np.abs(x[0]-x[-1])/len(x)

#We take dt=1/4*dx simply to ensure stability
dt=0.25*dx


cs=1 #Sound Speed

#Initialize f1, f2
f1=np.zeros([len(x)])
f2=f1
f1=1+0.05*np.exp(-100*(x-1/2)**2) #Initial Gaussian perturbation in density

#Initialize the J1 and J2 terms defined in the Hydro code example from Prof Eve J Lee
#J1plus is J_{1,j+1/2}, J1minus is J_{1,j-1/2}, same for J2.
J1plus=np.zeros([len(x)])
J1minus=np.zeros([len(x)])
J2plus=np.zeros([len(x)])
J2minus=np.zeros([len(x)])

#Iterative Scheme
for j in range(len(x)*3):
		#Velocities at t=j*dt (uplus and uminus are defined as in the Hydro code example)
		uplus=0.5*(f2/f1+np.roll(f2,-1)/np.roll(f1,-1))
		uminus=0.5*(f2/f1+np.roll(f2,1)/np.roll(f1,1))

		#The following variables locate where velocities are positive and negative in [0,1]
		posuplus=np.where(uplus>0)
		neguplus=np.where(uplus<=0)
		posuminus=np.where(uminus>0)
		neguminus=np.where(uminus<=0)

		### Update f1 ###
		J1plus[posuplus]=uplus[posuplus]*f1[posuplus]
		J1plus[neguplus]=uplus[neguplus]*np.roll(f1,-1)[neguplus]
		J1minus[posuminus]=uminus[posuminus]*np.roll(f1,1)[posuminus]
		J1minus[neguminus]=uminus[neguminus]*f1[neguminus]

		f1up=f1-dt/dx*(J1plus-J1minus) #update step

		#Rewrite boundary conditions for f1
		f1up[0]=f1[0]-dt/dx*J1plus[0]
		f1up[-1]=f1[-1]+dt/dx*J1minus[-1]
		f1=f1up

		### Update f2 ###
		J2plus[posuplus]=uplus[posuplus]*f2[posuplus]
		J2plus[neguplus]=uplus[neguplus]*np.roll(f2,-1)[neguplus]
		J2minus[posuminus]=uminus[posuminus]*np.roll(f2,1)[posuminus]
		J2minus[neguminus]=uminus[neguminus]*f2[neguminus]

		f2up=f2-dt/dx*(J2plus-J2minus) #update step

		#Rewrite boundary conditions for f2
		f2up[0]=f2[0]-dt/dx*J2plus[0]
		f2up[-1]=f2[-1]+dt/dx*J2minus[-1]
		f2=f2up

		### Update f2 with pressure gradient ###
		f2=f2up-dt/dx*cs**2*(np.roll(f1,-1)-np.roll(f1,1))

		
		#animation
		if j%10==0:
			plt.clf()
			plt.plot(x,f1)
			#plt.xlim([0,1])
			plt.ylim([0.9,1.2])
			plt.title('HydroSolver in 1D')
			plt.show()
			plt.pause(0.005)


