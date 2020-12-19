from itertools import product
import re
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
for m in messages:
    valid=True
    chunks=list(map(''.join, zip(*[iter(m)]*len(matched_by_rule['42'][0]))))    #chunks of lenght 8 because rules 42 and 31 create strings of lenght 8
    tokens=""
    for c in chunks:
        if c in matched_by_rule['42']:
            tokens+='42'
        elif c in matched_by_rule['31']:
            tokens+='31'
        else:
            valid=False
            break
    if valid and re.match(r"^(?:42)+(?:31)+$", tokens) and tokens.count('42') > tokens.count('31'):
        count+=1
print(f"p2: {count}")