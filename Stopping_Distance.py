import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


#m = 0.5 #(concrete, dry)
#m = 0.35 #(concrete, wet)
#m = 0.15 #(ice, dry)
#m = 0.08 #(ice, wet)


# distance covered over time 
# dxb =v0*tr + v0*t + (1/2*a*t**2)

# Situation parameters (in Kg, Km/h, meters & seconds)
v = input("Please Enter Initial Velocity of The Vehicle in Km/h:")
M=input("Please Enter The Mass of The Vehicle in tons:")
m=input("Please Enter The Dynamic Friction Coefficient According to Road Conditions:")
tr=input("Please Enter Driver's reaction Time!:")

v0 = float(v) * (1000/3600) 

MV = float(M) * 907.2  # mass in kg

wc= MV * 9.81   # weight of the car

#friction force in order to calc. deceleration 
fr = float(m) * float(wc)

a= -fr/MV

t = -v0/a
y = []
t1= []
#velocity over time
for i in np.arange(0 , t+float(tr)+1):
    if i <= float(tr) :
        print(i, "\t", format(v0, '.1f'))

        for i2 in range(int(v0)):

           y.append(v0)
           t1.append(i)
    
    elif i > float(tr):
    

        v0 = v0 + a
        y.append(v0)
        t1.append(i)
        print(i, "\t", format(v0, '.1f') ) 


        
#ploting the results


plt.plot(t1,y)
plt.title(f'Velocity profile of a car decelerating on a [Horizontal Plane] after reaction time of {tr} seconds'"\t" f'Dynamic friction coefficient = {m}' )
plt.xlabel("t(s)")
plt.ylabel("v(m/s)")
plt.grid()
plt.show()