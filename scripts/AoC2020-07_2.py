import re,functools

with open('../inputs/AoC2020-07.txt','r') as f :
    inp = f.read()

l = inp.replace('\n',' ').split('. ')[:-1]

notagraph = dict()

for rule in l :
    rule = rule.strip()
    container,contained = rule.split(' bags contain ')
    content = contained.split(', ')
    notagraph[container] = list()
    if 'no other bags' not in content :
        for bag in content :
            count = int(re.search('\d+',bag).group(0))
            color = re.search('(?<=\d ).+(?= bag)',bag).group(0)
            notagraph[container].append((count,color))
            if color not in notagraph :
                notagraph[color] = set()

def desc_count(color) :
    return sum([child[0]*(1+desc_count(child[1])) for child in notagraph[color]])

print(desc_count('shiny gold'))
