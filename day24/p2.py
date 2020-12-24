from collections import defaultdict
directions={'e':(0,1),'se':(1,1),'sw':(1,0),'w':(0,-1),'nw':(-1,-1),'ne':(-1,0)}

with open("day24/input.txt") as f:
    data=[list(l) for l in f.read().splitlines()]
tile_paths=[]
for i, d in enumerate(data):
    tile_paths.append([])
    while len(d)>0:
        c1=d.pop(0)
        tile_paths[i].append(c1 if c1 in directions else str(c1+d.pop(0)))
        
floor=defaultdict(bool)
for path in tile_paths:
    i, j =0, 0
    for ins in path:
        i+=directions[ins][0]
        j+=directions[ins][1]
    floor[(i,j)]=not floor[(i,j)]
print(f"p1: {list(floor.values()).count(True)}")

for _ in range(100):
    min_i=min(floor.keys(), key=lambda t: t[0])[0]-1
    max_i=max(floor.keys(), key=lambda t: t[0])[0]+2
    min_j=min(floor.keys(), key=lambda t: t[1])[1]-1
    max_j=max(floor.keys(), key=lambda t: t[1])[1]+2
    update=[]
    for i in range(min_i, max_i):
        for j in range(min_j, max_j):
            neighbours=[floor[(i+d[0], j+d[1])] for d in directions.values()].count(True)
            if (floor[(i,j)] and (neighbours==0 or neighbours>2)) or (not floor[(i,j)] and neighbours==2):
                update.append((i,j))
    for u in update:
        floor[u]=not floor[u]
print(f"p2: {list(floor.values()).count(True)}")