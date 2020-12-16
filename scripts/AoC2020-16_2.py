import re
from functools import reduce

notes_patt = re.compile('(.+): (\d+)-(\d+) or (\d+)-(\d+)')

def isvalid(ticket) :
    for value in ticket.split(',') :
        if int(value) not in valid :
            return False
    return True

fields = dict()
valid = list()
with open('../inputs/AoC2020-16.txt','r') as file :
    line = file.readline()
    while line != '\n' :
        match = notes_patt.search(line)
        field,r1start,r1end,r2start,r2end = match.groups()
        range1 = range(int(r1start),int(r1end)+1)
        range2 = range(int(r2start),int(r2end)+1)
        fields[field] = set(list(range1)+list(range2))
        valid.extend(fields[field])
        line = file.readline()

    valid = set(valid)
    file.readline()
    myticket = file.readline().split(',')

    file.readline()
    file.readline()
    
    possible = [list(fields.keys()) for k in range(len(fields))]
    for ticket in file :
        if isvalid(ticket) :
            for pos,value in enumerate(ticket.split(',')) :
                compatible = list()
                for field in possible[pos] :
                    if int(value) in fields[field] :
                        compatible.append(field)
                possible[pos] = compatible

allpos = range(len(possible))
for loop in allpos:
    for fields in possible :
        if len(fields) == 1 :
            for otherpos in allpos :
                if len(possible[otherpos]) > 1 and fields[0] in possible[otherpos] :
                    possible[otherpos].pop(possible[otherpos].index(fields[0]))

departure = [int(value) for pos,value in enumerate(myticket) if possible[pos][0].startswith('departure')]
print(reduce(lambda a,b : a*b,departure))
