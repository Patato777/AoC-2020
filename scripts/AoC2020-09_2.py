import functools

weakness = 373803594
with open('../inputs/AoC2020-09.txt','r') as file :
    fifou2 = list()
    total = 0
    while total != weakness :
        k = int(file.readline())
        while total+k > weakness :
            total -= fifou2.pop(0)
        total += k
        fifou2.append(k)

#If I wanted to use fifou2 really as a FIFO queue, I should calculate min and max as programme goes along
print(min(fifou2)+max(fifou2))
