with open('day15/input.txt') as f:
    start=[int(l) for l in f.read().strip().split(',')]
last_seen=dict()
for i,n in enumerate(start):
    last_seen[n]=i+1
prev=start[-1]
numiters=int(input("Input number of iterations: "))
for i in range(len(start),numiters):
    if prev not in last_seen.keys():
        last_seen[prev]=i
        prev=0
    else:
        aux=last_seen[prev]
        last_seen[prev]=i
        prev=i-aux
print(prev)