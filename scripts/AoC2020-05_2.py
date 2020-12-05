with open('../inputs/AoC2020-05.txt','r') as f :
    inp = f.readlines()

bindict = {'F':'0','B':'1','L':'0','R':'1'}

def seattobin(seat) :
    for zone,nb in bindict.items() :
        seat = seat.replace(zone,nb)
    return seat

l = [seattobin(seat).strip() for seat in inp]

takenseats = {(int(seat[:7],2),int(seat[7:],2)) for seat in l}
freeseats = {(i,j) for i in range(128) for j in range(8)}.difference(takenseats)

takenIDs = [8*seat[0]+seat[1] for seat in takenseats]
myID = [8*seat[0]+seat[1] for seat in freeseats if 8*seat[0]+seat[1]-1 in takenIDs and 8*seat[0]+seat[1]+1 in takenIDs][0]
print(myID)
