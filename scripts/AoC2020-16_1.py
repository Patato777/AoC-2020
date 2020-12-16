import re

notes_patt = re.compile('(\d+)-(\d+) or (\d+)-(\d+)')
valid = list()
with open('../inputs/AoC2020-16.txt','r') as file :
    line = file.readline()
    while line != '\n' :
        match = notes_patt.search(line)
        r1start,r1end,r2start,r2end = match.groups()
        range1 = range(int(r1start),int(r1end)+1)
        range2 = range(int(r2start),int(r2end)+1)
        valid.extend(list(range1)+list(range2))
        line = file.readline()

    while not line.startswith('nearby tickets:') :
        line = file.readline()

    error_rate = 0
    for line in file :
        for value in line.split(',') :
            if int(value) not in valid :
                error_rate += int(value)

print(error_rate)
