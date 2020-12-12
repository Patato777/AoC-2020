from math import radians,cos,sin

direc = {'N':1j,'S':-1j,'E':1,'W':-1}
turn = {0:1j,180:-1j,90:1,270:-1}

pos = 0
face = 90

with open('../inputs/AoC2020-12.txt','r') as file :
    for line in file :
        line = line.strip()
        command,value = line[0],int(line[1:])
        if command in direc :
            pos += direc[command]*value
        if line[0] == 'R' :
            face = (face+value)%360
        if line[0] == 'L' :
            face = (face-value)%360
        if line[0] == 'F' :
            pos += value*turn[face]

print(int(abs(pos.real)+abs(pos.imag)))
            
