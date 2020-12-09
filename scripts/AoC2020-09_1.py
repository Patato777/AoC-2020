import functools

with open('../inputs/AoC2020-09.txt','r') as file :
    fifou = [int(file.readline()) for k in range(25)]
    sums = [{k1+k2 for k2 in fifou[i+1:]} for i,k1 in enumerate(fifou)]
    k = int(file.readline())
    while k in functools.reduce(lambda s1,s2 : s1|s2, sums) :
        fifou.pop(0)
        sums.pop(0)
        for i,key in enumerate(fifou) :
            sums[i].add(key+k)
        sums.append(set())
        fifou.append(k)
        k = int(file.readline())

print(k)
