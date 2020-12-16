import re
classes_re=re.compile((r"^((?:\w ?)+): (\d+)-(\d+) or (\d+)-(\d+)$"))

with open('day16/input.txt') as f:
    data=f.read().replace("your ticket:\n", "").replace("\nnearby tickets:\n","").split('\n\n')
tickets=[[int(n) for n in t.split(',')] for t in data[1].splitlines()]
fields=dict()
for f in data[0].splitlines():
    match=classes_re.match(f)
    fields[match.group(1)]=((int(match.group(2)), int(match.group(3))),(int(match.group(4)), int(match.group(5))))
result=0
for t in tickets:
    for n in t:
        valid=False
        for f in fields.values():
            if not (n<f[0][0] or (n>f[0][1] and n<f[1][0]) or n>f[1][1]):
                valid=True
        if not valid:
            result+=n
print(result)