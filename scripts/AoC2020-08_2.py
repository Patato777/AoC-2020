with open('../inputs/AoC2020-08.txt','r') as f :
    inp = f.read()

l = inp.replace(' ','(').replace('\n',')\n').splitlines()+['end']

def acc(nb) :
    global accumulator
    accumulator += nb
    return 1

def nop(nb) :
    return 1

def jmp(nb) :
    return nb

def execute(code) :
    global stack
    point = 0
    while True :
        jump = eval(code[point])
        code[point] = 'loop'
        point += jump
        if code[point] == 'loop' :
            return False
        if code[point] == 'end' :
            return True
        if code[point][2] == 'p' :
            stack = [point] + stack

stack,finished,code = list(),False,l.copy()

while not finished :
    accumulator = 0
    finished = execute(code)
    code = l.copy()
    change = stack.pop()
    if code[change].startswith('jmp') :
        code[change] = code[change].replace('jmp','nop')
    else :
        code[change] = code[change].replace('nop','jmp')
    

print(accumulator)
