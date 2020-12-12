from collections import OrderedDict
with open('day12/input.txt') as f:
    data=[[l[0], int(l[1:])] for l in f.read().splitlines()]
directions=OrderedDict([('N',(-1,0)),('E',(0,1)),('S',(1,0)),('W',(0,-1))])
pos=[0,0]
facing='E'
for d in data:
    if d[0] in directions.keys():
        pos[0]+=d[1]*directions[d[0]][0]
        pos[1]+=d[1]*directions[d[0]][1]
    elif d[0]=='F':
        pos[0]+=d[1]*directions[facing][0]
        pos[1]+=d[1]*directions[facing][1]
    elif d[0]=='R':
        facing=list(directions.keys())[(list(directions.keys()).index(facing)+d[1]//90)%4]
    elif d[0]=='L':
        facing=list(directions.keys())[list(directions.keys()).index(facing)-d[1]//90]
print(abs(pos[0])+abs(pos[1]))