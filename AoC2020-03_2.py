with open('Aoc2020-03.txt','r') as f:
    inp = f.read()

l = inp.splitlines()
l2 = [l[k] for k in range(0,len(l),2)]

counts = list()

def slide(forest,right) :
    count,pos = 0,0
    width = len(l[0])
    for line in forest :
        t = [c for c in line]
        if line[pos] == '#' :
            count += 1
        pos = (pos+right)%width
    return count

for k in range(1,8,2) :
    counts.append(slide(l,k))
counts.append(slide(l2,1))

out = 1

for count in counts :
    out *= count

print(out)
