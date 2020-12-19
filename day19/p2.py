from itertools import product
matched_by_rule=dict()
def getPossibilities(rule):
    if rule in matched_by_rule:
        return matched_by_rule[rule]
    if rules[rule][0][0]=='a' or rules[rule][0][0]=='b':
        return rules[rule][0]
    pos_total=set()
    for option in rules[rule]:
        pos_op=[""]
        for r in option:
            pos_r=getPossibilities(r)
            pos_op=[pair[0]+pair[1] for pair in product(pos_op,pos_r)]
        for s in pos_op:
            pos_total.add(s)
    matched_by_rule[rule]=list(pos_total)
    return list(pos_total)

with open('day19/input.txt') as f:
    rules_raw, messages=f.read().replace('"', '').split('\n\n')
rules_raw=[l.split(': ') for l in rules_raw.splitlines()]
rules=dict()
for r in rules_raw:
    rules[r[0]]=[a.split(' ') for a in r[1].split(' | ')]
messages=messages.splitlines()
getPossibilities('0')
count=0
invalid_p1=[]
for m in messages:
    if m in matched_by_rule['0']:
        count+=1
    else:
        invalid_p1.append(m)
print(f"p1: {count}")
for m in invalid_p1:
    valid=True
    chunks=list(map(''.join, zip(*[iter(m)]*len(matched_by_rule['42'][0]))))    #chunks of lenght 8 because rules 42 and 31 create strings of lenght 8
    tokens=[]
    for c in chunks:
        if c in matched_by_rule['42']:
            tokens.append(42)
        elif c in matched_by_rule['31']:
            tokens.append(31)
        else:
            valid=False
    tail=tokens.count(31)
    head=tokens.count(42)
    if head <= tail or tail<1 or not valid:
        continue
    for i in range(head):
        if tokens[i]!=42:
            valid=False
    if valid:
        count+=1
print(f"p2: {count}")