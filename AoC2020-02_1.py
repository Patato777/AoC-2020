with open('AoC2020-02.txt','r') as f :
    inp = f.readlines()

count = 0
for elem in inp :
    pwd = elem.split()
    beg,end = pwd[0].split('-')
    if int(beg) <= pwd[2].count(pwd[1][:-1]) <= int(end) :
        count += 1
        
print(count)
