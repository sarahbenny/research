import numpy as np
import math
from matplotlib.pyplot import plot

distances=[0.6,0.8]
#d=0.6
w=0.2
r_grid = np.arange(0.6,1.0,0.1)
print(r_grid)
f = np.zeros(len(r_grid))
#g = np.zeros(len(r_grid))
b = 1/(w*math.sqrt(math.pi)) #b is fine
print('b='+str(b)+'\n')
a=[]
for r in range(len(r_grid)):
    a.append(1/(r_grid[r]*r_grid[r]*2)) #a is fine
    for d in distances:
        diff = r_grid[r]-d
        #print('a='+str(a)+',diff='+str(diff)+'\n')
        f[r] = f[r] + b*math.exp(-(diff*diff)/(w*w))
#print(f[0])
#print(f[1])
#print(f[2])
#print(f[3])
g = np.multiply(a,f)
print(g)
