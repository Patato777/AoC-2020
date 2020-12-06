with open('../inputs/AoC2020-06.txt','r') as f :
    count = 0
    answers = set()
    endofgroup = True
    for line in f :
        if line == '\n' :
            count += len(answers)
            answers = set()
            endofgroup = True
            line = f.readline()
        if endofgroup :
            answers = set(line.strip())
            endofgroup = False
        else :
            answers = answers.intersection(set(line.strip()))

print(count+len(answers))
