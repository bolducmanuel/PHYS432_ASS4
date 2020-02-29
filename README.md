# PHYS432_ASS4
Manuel Bolduc (260788246)

Version of Python used: 3.x

## Codes
### Advection.py
This code solves the 1D advection equation on the interval [0,1] for a constant speed of u=-0.1. We use both the FTCS and the Lax Friedrichs (LF) method. As it can be seen when running the code, FTCS grows unstable, whereas LF remains stable, as expected. Our animation shows the density evolution over time

### HydroSolver.py
This code solves the conservative form of hydro equations on the interval [0,1]. We consider a gas with 0 initial velocity, and a small inital gaussian perturbation for the density. Our animation shows the density evolution over time. 

As we increase the amplitude of the initial perturbation, we can indeed see a schock. In our code, we set the initial amplitude of the gaussian to 0.05*(rho). However, when the amplitude of the gaussian is in the order of 1/2*(rho), we clearly see a shock as the waves come back to the center. The width of the shock is related to the ratio between dt and dx. 

## Collaborators

For the HydroSolver problem, I worked with Mathieu Bruneault and Alex Khoury.


