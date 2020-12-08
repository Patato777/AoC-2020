with open('../inputs/AoC2020-08.txt','r') as f :
    inp = f.read()

l = inp.replace(' ','(').replace('\n',')\n').splitlines()

def acc(nb) :
    global accumulator
    accumulator += nb
    return 1

def nop(nb) :
    return 1

def jmp(nb) :
    return nb
    
accumulator,point,looped = 0,0,False
while not looped :
    jump = eval(l[point])
    l[point] = 'loop'
    point += jump
    if l[point] == 'loop' :
        looped = True
    
print(accumulator)
