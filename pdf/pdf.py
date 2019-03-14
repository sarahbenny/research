import numpy as np
import math
from matplotlib.pyplot import plot

distances=[0.9,1.2,1.5,1.0]
w=0.2 
r_grid = np.arange(0.1, 2 + 1.1 * 0.1, 0.1)
print(r_grid)
f = np.zeros(len(r_grid))
#g = np.zeros(len(r_grid))
b = 1/(w*math.sqrt(math.pi))
#print('b='+str(b)+'\n')
a=[]
for r in range(len(r_grid)):
    a.append(1/(r_grid[r]*r_grid[r]*4))
    for d in distances:
        diff = r_grid[r]-d
        #print('a='+str(a)+',diff='+str(diff)+'\n')
        f[r] = f[r] + b*math.exp(-(diff*diff)/(w*w))
g = np.multiply(a,f)
print(g)
