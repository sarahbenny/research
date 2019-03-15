from ase.io import iread
from ase.io import write
from ase import Atoms
import sys
import numpy as np
import math

#Usage: python get_distances.py [md_car_file] [elements_file]

md_car_file=sys.argv[1]
el_file=sys.argv[2]
el=open(el_file)
elements=''
n_atoms=0
for line in el:
   elements=elements+line.rstrip()
   n_atoms=n_atoms+1
md_car=open(md_car_file)
lines=md_car.readlines()
n_steps=len(lines)/(n_atoms+7)
for i in range(n_steps):
    a=lines[2+(n_atoms+7)*i]
    ax,ay,az=a.split()
    ax=float(ax)
    ay=float(ay)
    az=float(az)
    a_mag=math.sqrt(ax*ax+ay*ay+az*az)

    b=lines[3+(n_atoms+7)*i]
    bx,by,bz=b.split()
    bx=float(bx)
    by=float(by)
    bz=float(bz)
    b_mag=math.sqrt(bx*bx+by*by+bz*bz)


    c=lines[4+(n_atoms+7)*i]
    cx,cy,cz=c.split()
    cx=float(cx)
    cy=float(cy)
    cz=float(cz) 
    c_mag=math.sqrt(cx*cx+cy*cy+cz*cz)

    coords=[]
    oh=[]
    hh=[]
    for j in range(7,(n_atoms+7)):
        x, y, z=lines[j+(n_atoms+7)*i].split()
        coords.append([a_mag*float(x), b_mag*float(y), c_mag*float(z)])
    atoms=Atoms(elements,positions=coords,cell=[[ax,ay,az],[bx,by,bz],[cx,cy,cz]])
    distances=np.asarray(atoms.get_all_distances(mic=True))
    for i in range(n_atoms):
        for j in range(i,n_atoms): #because distance matrix is symmetric
            if ( (elements[i] == 'H' and elements[j] == 'O') or (elements[i] == 'O' and elements[j] == 'H') ):
                oh.append(distances[i][j])
            if ( (elements[i] == 'H' and elements[j] == 'H') or (elements[i] == 'H' and elements[j] == 'H') ):
                hh.append(distances[i][j])

md_car.close
