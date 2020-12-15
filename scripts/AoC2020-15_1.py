with open('../inputs/AoC2020-15.txt','r') as f :
    starting = eval('['+f.read()+']')

seen = dict()
for turn,value in enumerate(starting[:-1]) :
    seen[value] = turn+1

prev = starting[-1]

for turn in range(len(starting)+1,2021) :
    if prev in seen :
        new = turn-1-seen[prev]
    else :
        new = 0
    seen[prev] = turn-1
    prev = new

print(new)
