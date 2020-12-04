with open('../inputs/AoC2020-02.txt','r') as f :
    inp = f.readlines()

count = 0
for elem in inp :
    pwd = elem.split()
    k1,k2 = pwd[0].split('-')
    if (pwd[2][int(k1)-1]+pwd[2][int(k2)-1]).count(pwd[1][:-1]) == 1 :
        count += 1

print(count)
