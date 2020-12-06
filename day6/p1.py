with open('day6/input.txt') as f:
    data=[l.replace('\n','') for l in f.read().split('\n\n')]
print(sum([len(set(group)) for group in data]))