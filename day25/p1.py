divisor=20201227
subject=7
with open("day25/input.txt") as f:
    public_keys=[int(l) for l in f.read().splitlines()]
loops=[]
for key in public_keys:
    value=1
    loop_size=0
    while value!=key:
        value*=subject
        value%=divisor
        loop_size+=1
    loops.append(loop_size)
value=1
for _ in range(loops[0]):
    value*=public_keys[1]
    value%=divisor
print(value)