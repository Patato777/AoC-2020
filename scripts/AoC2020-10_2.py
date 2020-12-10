from functools import reduce

with open('../inputs/AoC2020-10.txt','r') as f :
    l = sorted([0]+[int(k) for k in f.readlines()])

l.append(l[-1]+3)

passage = [0]+[k for k in range(len(l)-1) if l[k+1]-l[k-1] == 6]+[len(l)]

def rec(k,m) :
    att = [l[k]+j for j in [1,2,3]]
    if k+1 == m :
        return 1
    else :
        tot = rec(k+1,m)
        if k+2 < m and l[k+2] in att :
            tot += rec(k+2,m)
        if k+3 < m and l[k+3] in att :
            tot += rec(k+3,m)
        return tot

morceaux = [rec(passage[k],passage[k+1]) for k in range(len(passage)-1)]
print(reduce(lambda a,b : a*b, morceaux))
