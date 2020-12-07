def getColors(color):
    colors=set()
    if color not in inverseRules.keys():
        return colors
    for c in inverseRules[color]:
        colors.add(c)
        colors.update(getColors(c))
    return(colors)

with open('day7/input.txt') as f:
    rules=dict([l.split(' contain') for l in f.read().replace(' bags', '').replace(' bag', '').replace('.', '').replace(' no other', '0 ').splitlines()])
for key in rules:
    rules[key]=[d[2:].strip() for d in rules[key].split(', ')]
inverseRules=dict() #key is contained directly by value
for key in rules:
    for color in rules[key]:
        if color not in inverseRules.keys():
            inverseRules[color]=[key]
        else:
            inverseRules[color].append(key)
print(len(getColors('shiny gold')))