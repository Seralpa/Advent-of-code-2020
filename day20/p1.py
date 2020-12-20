from day20.Tile import Tile
from functools import reduce
def get_corners(tiles):
    corners=[]
    for t in tiles:
        if len(t.get_adjacent(tiles))==2:
            corners.append(t)

with open('day20/input.txt') as f:
    data=[d.splitlines() for d in f.read().split('\n\n')]
tiles=[]
for d in data:
    id_=d.pop(0)
    tiles.append(Tile(int(id_[5:-1]), d))
print(reduce((lambda x, y: x.id * y.id), get_corners(tiles)))