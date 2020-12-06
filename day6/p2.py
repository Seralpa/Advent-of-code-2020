with open('day6/test.txt') as f:
    data=[map(set, l.splitlines()) for l in f.read().split('\n\n')]
print(sum([len(set.intersection(*group)) for group in data]))