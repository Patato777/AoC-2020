import numpy as np

with open('../inputs/AoC2020-17.txt','r') as f :
    inp = [list(line.replace('.','0').replace('#','1').rstrip()) for line in f]

neighbours = [(i,j,k,l) for i in range(-1,2) for j in range(-1,2) for k in range(-1,2) for l in range(-1,2) if (i,j,k,l) != (0,0,0,0)]

space = np.zeros((15,15,22,22))
space[7,7,7:15,7:15] = inp

for cycle in range(6) :
    workspace = np.copy(space)
    for w in range(6-cycle,9+cycle) :
        for z in range(6-cycle,9+cycle) :
            for x in range(6-cycle,16+cycle) :
                for y in range(6-cycle,16+cycle) :
                    count = sum([space[w+i,z+j,x+k,y+l] for i,j,k,l in neighbours])
                    if space[w,z,x,y] :
                        if count not in {2,3} :
                            workspace[w,z,x,y] = 0
                    else :
                        if count == 3 :
                            workspace[w,z,x,y] = 1
    space = np.copy(workspace)

print(np.count_nonzero(space))
