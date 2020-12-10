with open('../inputs/AoC2020-10.txt','r') as f :
    inp = f.read()

nb = [int(n) for n in inp.splitlines()]

output = max(nb)

sorted_nb = sorted(nb)

diff1,diff3 = 0,1
prev = 0
for k in sorted_nb :
    if k-prev == 1 :
        diff1 += 1
    elif k-prev == 3 :
        diff3 += 1
    prev = k

print(diff1*diff3)
