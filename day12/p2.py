def rotate_right(pos, angle):
    aux=pos[0]
    if angle==90:
        pos[0]=pos[1]
        pos[1]=0-aux
    elif angle==180:
        pos[0]=0-pos[0]
        pos[1]=0-pos[1]
    elif angle==270:
        pos[0]=0-pos[1]
        pos[1]=aux

with open('day12/input.txt') as f:
    data=[[l[0], int(l[1:])] for l in f.read().splitlines()]
directions={'N':(-1,0),'E':(0,1),'S':(1,0),'W':(0,-1)}
shipPos=[0,0]
wayPos=[-1,10]#relative to ship
for d in data:
    if d[0] in directions.keys():
        wayPos[0]+=d[1]*directions[d[0]][0]
        wayPos[1]+=d[1]*directions[d[0]][1]
    elif d[0]=='F':
        shipPos[0]+=d[1]*wayPos[0]
        shipPos[1]+=d[1]*wayPos[1]
    elif d[0]=='R':
        rotate_right(wayPos, d[1])
    elif d[0]=='L':
        rotate_right(wayPos, 360-d[1])
print(abs(shipPos[0])+abs(shipPos[1]))