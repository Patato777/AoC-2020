import functools

weakness = 373803594
with open('../inputs/AoC2020-09.txt','r') as file :
    fifou2 = list()
    while sum(fifou2) != weakness :
        k = int(file.readline())
        while sum(fifou2)+k > weakness :
            fifou2.pop(0)
        fifou2.append(k)

print(min(fifou2)+max(fifou2))
