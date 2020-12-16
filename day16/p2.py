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
tickets_to_remove=[]
for t in tickets:
    valid_ticket=True
    for n in t:
        valid_num=False
        for f in fields.values():
            if not (n<f[0][0] or (n>f[0][1] and n<f[1][0]) or n>f[1][1]):
                valid_num=True
                break
        if not valid_num:
            valid_ticket=False
            break
    if not valid_ticket:
        tickets_to_remove.append(t)
for t in tickets_to_remove:
    tickets.remove(t)

possible_places=dict()
for f in fields:
    possible_places[f]=list(range(0, len(tickets[0])))

for t in tickets:
    for i, n in enumerate(t):
        for k, f in fields.items():
            if n<f[0][0] or (n>f[0][1] and n<f[1][0]) or n>f[1][1]:
                if i in possible_places[k]:
                    possible_places[k].remove(i)

for i in range(100):
    for i in range(len(tickets[0])):
        fields_contain_i=[k for k, v in possible_places.items() if i in v]
        if len(fields_contain_i)==1:
            possible_places[fields_contain_i[0]].clear()
            possible_places[fields_contain_i[0]].append(i)
    for k,v in possible_places.items():
        if len(v)==1:
            for kaux in possible_places:
                if kaux!=k and possible_places[k][0] in possible_places[kaux]:
                    possible_places[kaux].remove(possible_places[k][0])
result=1
for k,v in possible_places.items():
    if k.startswith('departure'):
        if len(v)>1:
            print("ERROR! input too complex!")
        result*=tickets[0][v[0]]
print(result)