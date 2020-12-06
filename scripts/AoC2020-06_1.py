with open('../inputs/AoC2020-06.txt','r') as f :
    count = 0
    answers = set()
    for line in f :
        if line == '\n' :
            count += len(answers)
            answers = set()
        answers = answers.union(set(line.strip()))

print(count+len(answers))
