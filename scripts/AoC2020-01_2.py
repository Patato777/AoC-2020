with open('../inputs/AoC2020-01.txt','r') as f :
    inp = f.readlines()

l = [int(line[:-1]) for line in inp]
for i,n1 in enumerate(l):
    for j,n2 in enumerate(l[i:]) :
        for k,n3 in enumerate(l[j:]) :
            if n1+n2+n3 == 2020 :
                print(n1,n2,n3,n1*n2*n3)
