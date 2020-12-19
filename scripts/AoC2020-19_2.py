import re

with open('../inputs/AoC2020-19.txt','r') as f :
    rules = dict()
    messages = list()
    rulpat = re.compile(r'(\d+): (.+)')
    line = f.readline()
    while line != '\n' :
        number,rule = rulpat.search(line).groups()
        rules[int(number)] = rule.replace('"','')
        line = f.readline()
    for line in f :
        messages.append(line.rstrip())

rules[8] = '42 | 42 8'
rules[11] = '42 31 | 42 11 31'
def parse_rule (rule,n):
    if rule.isalpha() :
        return rule
    elif '|' in rule :
        p1,p2 = rule.split('|')
        if n > 8 :
            return parse_rule(p1.rstrip(),0)
        return '('+parse_rule(p1.rstrip(),0)+'|'+parse_rule(p2.lstrip(),n+1)+')'
    else :
        return ''.join([parse_rule(rules[int(r)],n) for r in rule.split()])

pattern = re.compile(parse_rule(rules[0],0))
print(len([m for m in messages if pattern.fullmatch(m)]))
