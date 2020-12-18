with open('../inputs/AoC2020-18.txt','r') as file :
    homeworks = [line.replace(' ','').rstrip() for line in file]

def find_par(expr) :
    par = 0
    for k,char in enumerate(expr) :
        if char == '(' :
            par += 1
        elif char == ')' :
            par -= 1
        if par == -1 :
            return k
    return k

def recvaluate(expr) :
    point = 0
    result = 0
    op = '+'
    while point < len(expr) :
        char = expr[point]
        if char.isdigit() :
            result = eval(f'{result}{op}{char}')
            point += 1
        elif char == '(' :
            end_p = point+find_par(expr[point+1:])+1
            tot = recvaluate(expr[point+1:end_p])
            result = eval(f'{result}{op}{tot}')
            point = end_p + 1
        else :
            op = char
            point += 1
    return result

print(sum(map(recvaluate,homeworks)))
