with open('../inputs/AoC2020-05.txt','r') as f :
    inp = f.readlines()

bindict = {'F':'0','B':'1','L':'0','R':'1'}

def seattobin(seat) :
    for zone,nb in bindict.items() :
        seat = seat.replace(zone,nb)
    return seat

l = [seattobin(seat).strip() for seat in inp]

print(max([8*int(seat[:7],2)+int(seat[7:],2) for seat in l]))
