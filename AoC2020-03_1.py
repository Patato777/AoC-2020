with open('Aoc2020-03.txt','r') as f:
    inp = f.read()

l = inp.splitlines()
count,pos = 0,0
width = len(l[0])
for line in l :
    t = [c for c in line]
    if line[pos] == '#' :
        count += 1
        t[pos] = 'X'
    else :
        t[pos] = 'O'
    print(''.join(t))
    pos = (pos+3)%width

print(count)
