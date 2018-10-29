# Orbitas keplerianas

import numpy as np
import math

numIt=100
step=10*365*2*math.pi/numIt
U=np.empty((4*numIt,1))
U[0,0]=1
U[1,0]=0
U[2,0]=0
U[3,0]=1

def F(U,i):
    return np.matrix([[U[2*i+2,0]],[U[2*i+3,0]],[-U[2*i,0]/((U[2*i,0]**2+U[2*i+1,0]**2)**(3/2))],[-U[1,0]/((U[0,0]**2+U[1,0]**2)**(3/2))]])

for i in range(numIt):
    
    U[2*i+4]=U[2*i]+step*F(U,i)
    U[2*i+5]=U[2*i+1]+step*F(U)