from math import radians,cos,sin

direc = {'N':1j,'S':-1j,'E':1,'W':-1}
turn = {'R':-1,'L':1}

pos = 0
waypoint = 10+1j


with open('../inputs/AoC2020-12.txt','r') as file :
    for line in file :
        line = line.strip()
        command = line[0]
        value = int(line[1:])
        if command in direc :
            waypoint += direc[command]*value
        if command in turn :
            angle = turn[command]*radians(value)
            waypoint *= cos(angle) + 1j*sin(angle)
        if command == 'F' :
            pos += value*waypoint

print(int(abs(pos.real)+abs(pos.imag)))
