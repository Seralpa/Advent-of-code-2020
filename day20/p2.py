from day20.Tile import Tile
import numpy as np

def get_corner(tiles):
    for t in tiles:
        if len(t.get_adjacent(tiles))==2:
            return t

def count_monsters(image):
    monsters=0
    for i in range(2, len(image)):          #2 cause height of monster
        for j in range(len(image[0])-20):   #20 cause of lenght of monster
            if image[i-0][j+1]=='#' and image[i-0][j+4]=='#' and image[i-0][j+7]=='#' and image[i-0][j+10]=='#' and image[i-0][j+13]=='#' and image[i-0][j+16]=='#' and image[i-1][j+0]=='#' and image[i-1][j+5]=='#' and image[i-1][j+6]=='#' and image[i-1][j+11]=='#' and image[i-1][j+12]=='#' and image[i-1][j+17]=='#' and image[i-1][j+18]=='#' and image[i-1][j+19]=='#' and image[i-2][j+18]=='#':
                monsters+=1
    return monsters

with open('day20/input.txt') as f:
    data=[d.splitlines() for d in f.read().split('\n\n')]
tiles=[]
for d in data:
    id_=d.pop(0)
    tiles.append(Tile(int(id_[5:-1]), d))
top_corner=get_corner(tiles)
matching_sides=[top_corner.is_adjacent(t)[0] for t in top_corner.get_adjacent(tiles)]
while matching_sides!=[1,2] and matching_sides!=[2,1]:
    top_corner.rotate_right()
    matching_sides[0]=(matching_sides[0]+1)%4
    matching_sides[1]=(matching_sides[1]+1)%4
tile_image=[]
i=0
first_in_line=top_corner
while first_in_line:
    tile_image.append([])
    current=first_in_line
    first_in_line=first_in_line.get_adjacent_down(tiles)
    while current:
        tile_image[i].append(current)
        current=current.get_adjacent_right(tiles)
    i+=1
        
image=np.block([[t.matrix for t in l] for l in tile_image])
count=0
for _ in range(2):
    for _ in range(2):
        for _ in range(4):
            count=max(count_monsters(image), count)
            image=np.rot90(image)
        image=np.fliplr(image)
    image=np.flipud(image)
print(dict(zip(*np.unique(image, return_counts=True)))['#']-count*15)