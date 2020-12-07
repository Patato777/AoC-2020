import re,functools

with open('../inputs/AoC2020-07.txt','r') as f :
    inp = f.read()

l = inp.replace('\n',' ').split('. ')[:-1]

notagraph = dict()

for rule in l :
    rule = rule.strip()
    container,contained = rule.split(' bags contain ')
    content = contained.split(', ')
    if 'no other bags' not in content :
        for bag in content :
            color = re.search('(?<=\d ).+(?= bag)',bag).group(0)
            if color not in notagraph :
                notagraph[color] = {container}
            else :
                notagraph[color].add(container)
    if container not in notagraph :
        notagraph[container] = set()

def down_the_graph(color) :
    children = notagraph[color]
    desc = [children] + [down_the_graph(col) for col in children]
    return functools.reduce(lambda s1,s2 : s1|s2,desc)

print(len(down_the_graph('shiny gold')))
