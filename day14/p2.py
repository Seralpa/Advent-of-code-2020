import re
mask_re=re.compile(r"^mask = ((?:X|1|0){36})$")
write_re=re.compile(r"^mem\[(\d+)\] = (\d+)$")
with open('day14/input.txt') as f:
    data=f.read().splitlines()
mem=dict()
for d in data:
    if mask_re.match(d):
        mask=mask_re.match(d).group(1)
    elif write_re.match(d):
        index=format(int(write_re.match(d).group(1)), '036b')
        value=int(write_re.match(d).group(2))
        addresses=['']
        for mb, ib in zip(mask, index):
            if mb=='0':
                addresses=[a+ib for a in addresses]
            elif mb=='1':
                addresses=[a+'1' for a in addresses]
            elif mb=='X':
                addresses+=addresses[:]
                addresses=[a + ('0' if i<len(addresses)//2 else '1') for i, a in enumerate(addresses)]
        for a in addresses:
            mem[a]=value
print(sum(mem.values()))