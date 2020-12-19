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

def parse_rule (rule):
    if rule.isalpha() :
        return rule
    elif '|' in rule :
        p1,p2 = rule.split('|')
        return '('+parse_rule(p1.rstrip())+'|'+parse_rule(p2.lstrip())+')'
    else :
        return ''.join([parse_rule(rules[int(r)]) for r in rule.split()])

pattern = re.compile(parse_rule(rules[0]))
print(len([m for m in messages if pattern.fullmatch(m)]))
