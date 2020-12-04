import re

with open('../inputs/AoC2020-04.txt') as f :
    inp = f.read()

l = inp.split('\n\n')
l = [' '+e.replace('\n',' ')+' ' for e in l]

reg = [re.compile('(?<=\sbyr:)\d{4}(?=\s)'),\
       re.compile('(?<=\siyr:)\d{4}(?=\s)'),\
       re.compile('(?<=\seyr:)\d{4}(?=\s)'),\
       re.compile('(?<=\shgt:)\d+(cm|in)(?=\s)'),\
       re.compile('(?<=\shcl:)#[0-9a-f]{6}(?=\s)'),\
       re.compile('(?<=\secl:)amb|blu|brn|gry|grn|hzl|oth(?=\s)'),\
       re.compile('(?<=\spid:)\d{9}(?=\s)')]
cond = [lambda s : int(s) in range(1920,2003),\
        lambda s : int(s) in range(2010,2021),\
        lambda s : int(s) in range(2020,2031),\
        lambda s : int(s[:-2]) in range(150,194) if s.endswith('cm') else int(s[:-2]) in range(59,77),\
        lambda s : True,\
        lambda s : True,\
        lambda s : True]

count = 0
for entry in l :
    isValid = True
    for k,regex in enumerate(reg) :
        m = regex.search(entry)
        if not m or not cond[k](m.group(0)) :
            isValid = False
    if isValid :
        count += 1

print(count)
