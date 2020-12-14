import re
mask_re=re.compile(r"^mask = ((?:X|1|0){36})$")
write_re=re.compile(r"^mem\[(\d+)\] = (\d+)$")
with open('day14/input.txt') as f:
    data=[l for l in f.read().splitlines()]
mem=dict()
for d in data:
    if mask_re.match(d):
        mask=mask_re.match(d).group(1)
    elif write_re.match(d):
        index=write_re.match(d).group(1)
        value=format(int(write_re.match(d).group(2)), '036b')
        result=''
        for mb, vb in zip(mask, value):
            result += vb if mb=='X' else mb
        mem[index]=int(result,2)
print(sum(mem.values()))