with open('../inputs/AoC2020-13.txt','r') as f :
    min_ts = int(f.readline())
    bus = f.readline().strip().split(',')

departures = [(-k,int(b)) for k,b in enumerate(bus) if b != 'x']


def bezout(a,b) :
    upre,uc = 1,0
    vpre,vc = 0,1
    while b != 1 :
        b1 = b
        q,b = divmod(a,b)
        a = b1
        upre,uc = uc, upre+(-1)*uc*q
        vpre,vc = vc, vpre+(-1)*vc*q
    return uc,vc

eq = departures[0]

for d in departures[1:] :
    bez = bezout(eq[1],d[1])
    a = d[0]*eq[1]*bez[0]+eq[0]*d[1]*bez[1]
    eq = (a%(eq[1]*d[1]),eq[1]*d[1])

print(eq[0])
