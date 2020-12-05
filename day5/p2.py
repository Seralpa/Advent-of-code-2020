with open("day5/input.txt") as f:
    data=f.read().splitlines()
ids=set()
for d in data:
    row, col = 0, 0
    for i, c in enumerate(d[:7]):
        if c=='B':
            row+= 2**(6-i)
    for i, c in enumerate(d[-3:]):
        if c=='R':
            col+= 2**(2-i)
    ids.add(row*8+col)
print(set(range(min(ids), max(ids)))-ids)