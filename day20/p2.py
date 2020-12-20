class Tile:
    def __init__(self, id_, matrix):
        self.id=id_
        self.matrix=[list(l) for l in matrix]
        self.sides=self.get_sides()
        self.trim_edges()
    
    def trim_edges(self):
        self.matrix.pop(0)
        self.matrix.pop()
        for l in self.matrix:
            l.pop(0)
            l.pop()

    def get_sides(self):
        return [list(self.matrix[0]), 
                [self.matrix[i][-1] for i in range(len(self.matrix))],
                list(self.matrix[-1]), 
                [self.matrix[i][0] for i in range(len(self.matrix))]]
    
    def __eq__(self, other):
        return self.id == other.id
    
    def is_adjacent(self, other):
        if self==other:
            return False
        for i, s1 in enumerate(self.sides):
            for j, s2 in enumerate(other.sides):
                if s1==s2 or list(reversed(s1))==s2:
                    return (i, j)
        return False
    
    def rotate_right(self):
        self.matrix=rotate_matrix(self.matrix)
        self.sides=self.sides[-1:]+self.sides[:-1]
        self.sides[0].reverse()
        self.sides[2].reverse()
    
    def get_adjacent(self, rest):
        adjacent=[]
        for t2 in tiles:
            matching_sides=self.is_adjacent(t2)
            if matching_sides:
                while (matching_sides[0]-matching_sides[1])==0 or (matching_sides[0]-matching_sides[1])%2!=0:
                    t2.rotate_right()
                    matching_sides=self.is_adjacent(t2)
                adjacent.append(t2)
        return adjacent

    def get_adjacent_right(self, rest):
        for t2 in tiles:
            matching_sides=self.is_adjacent(t2)
            if matching_sides and matching_sides[0]==1:
                while (matching_sides[0]-matching_sides[1])==0 or (matching_sides[0]-matching_sides[1])%2!=0:
                    t2.rotate_right()
                    matching_sides=self.is_adjacent(t2)
                if self.sides[matching_sides[0]] != t2.sides[matching_sides[1]]:
                    t2.flip_horizontal_axis()
                return t2
        return False

    def get_adjacent_down(self, rest):
        for t2 in tiles:
            matching_sides=self.is_adjacent(t2)
            if matching_sides and matching_sides[0]==2:
                while (matching_sides[0]-matching_sides[1])==0 or (matching_sides[0]-matching_sides[1])%2!=0:
                    t2.rotate_right()
                    matching_sides=self.is_adjacent(t2)
                if self.sides[matching_sides[0]] != t2.sides[matching_sides[1]]:
                    t2.flip_vertical_axis()
                return t2
        return False
    
    def flip_horizontal_axis(self):
        self.matrix.reverse()
        self.sides[0], self.sides[2]=self.sides[2], self.sides[0]
        self.sides[1].reverse()
        self.sides[3].reverse()
    
    def flip_vertical_axis(self):
        for l in self.matrix:
            l.reverse()
        self.sides[1], self.sides[3]=self.sides[3], self.sides[1]
        self.sides[0].reverse()
        self.sides[2].reverse()

def rotate_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        li = list(map(lambda x: x[i], matrix))
        li.reverse()
        new_matrix.append(li)
    return new_matrix

def count_monsters(image):
    count=0
    for i in range(2, len(image)):          #2 cause height of monster
        for j in range(len(image[0])-20):   #20 cause of lenght of monster
            if image[i-0][j+1]=='#' and image[i-0][j+4]=='#' and image[i-0][j+7]=='#' and image[i-0][j+10]=='#' and image[i-0][j+13]=='#' and image[i-0][j+16]=='#' and image[i-1][j+0]=='#' and image[i-1][j+5]=='#' and image[i-1][j+6]=='#' and image[i-1][j+11]=='#' and image[i-1][j+12]=='#' and image[i-1][j+17]=='#' and image[i-1][j+18]=='#' and image[i-1][j+19]=='#' and image[i-2][j+18]=='#':
                count+=1
    return count

with open('day20/input.txt') as f:
    data=[d.splitlines() for d in f.read().split('\n\n')]
tiles=[]
for d in data:
    id_=d.pop(0)
    tiles.append(Tile(int(id_[5:-1]), d))
top_corner=tiles[28]    #from part 1
# top_corner=tiles[1]
top_corner_adjacent=top_corner.get_adjacent(tiles)
matching_sides=[]
for t in top_corner_adjacent:
    matching_sides.append(top_corner.is_adjacent(t)[0])
while matching_sides!=[1,2] and matching_sides!=[2,1]:
    top_corner.rotate_right()
    matching_sides[0]=(matching_sides[0]+1)%4
    matching_sides[1]=(matching_sides[1]+1)%4
tile_image=[]
first_in_line=top_corner
i=0
while True:
    if not first_in_line:
        break
    tile_image.append([])
    current=first_in_line
    first_in_line=first_in_line.get_adjacent_down(tiles)
    while True:
        tile_image[i].append(current)
        next_tile=current.get_adjacent_right(tiles)
        if next_tile:
            current=next_tile
        else:
            i+=1
            break
        
image=[]
for i,l in enumerate(tile_image):
    image+=[[] for _ in range(len(l[0].matrix))]
    for t in l:
        for j in range(len(t.matrix)):
            image[i*len(t.matrix)+j]+=t.matrix[j]
count=0
for _ in range(2):
    for _ in range(2):
        for _ in range(4):
            count=max(count_monsters(image), count)
            image=rotate_matrix(image)
        image.reverse()
    for l in image:
        l.reverse()
roughness =0
for l in image:
    roughness+=l.count('#')
print(roughness-count*15)
