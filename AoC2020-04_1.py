import re

with open('AoC2020-04.txt') as f :
    inp = f.read()

l = inp.split('\n\n')
fields = ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']

count = 0

for entry in l :
    isValid = True
    for field in fields :
        if entry.find(field) == -1 :
            isValid = False
    if isValid :
        count += 1

print(count)
