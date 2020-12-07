def getNumBags(color):
    if color=='':
        return 0
    numBags=1
    for bag in rules[color]:
        numBags+=bag[1]*getNumBags(bag[0])
    return numBags

with open('day7/input.txt') as f:
    rules=dict([l.split(' contain') for l in f.read().replace(' bags', '').replace(' bag', '').replace('.', '').replace(' no other', '0 ').splitlines()])
for key in rules:
    rules[key]=[(d[2:].strip(), int(d[:2].strip())) for d in rules[key].split(', ')]
print(getNumBags('shiny gold')-1)   #-1 cause shiny bag not included