with open('../inputs/AoC2020-13.txt','r') as f :
    min_ts = int(f.readline())
    bus = f.readline().strip().split(',')

departures = [(min_ts+int(b)-(min_ts%int(b)),b) for b in bus if b != 'x']
next_d = min(departures,key = lambda i : i[0])

print((next_d[0]-min_ts)*int(next_d[1]))
