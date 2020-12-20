import numpy as np
class Tile:
    def __init__(self, id_, matrix):
        self.id=id_
        self.matrix=[list(l) for l in matrix]
        self.sides=self.get_sides()
        self.trim_edges()
        self.matrix=np.array(self.matrix)
    
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

    def __array__(self):
        return self.matrix
    
    def is_adjacent(self, other):
        if self==other:
            return False
        for i, s1 in enumerate(self.sides):
            for j, s2 in enumerate(other.sides):
                if s1==s2 or list(reversed(s1))==s2:
                    return (i, j)
        return False
    
    def rotate_right(self):
        self.matrix=np.rot90(self.matrix, k=3)
        self.sides=self.sides[-1:]+self.sides[:-1]
        self.sides[0].reverse()
        self.sides[2].reverse()
    
    def get_adjacent(self, tiles):
        adjacent=[]
        for t2 in tiles:
            matching_sides=self.is_adjacent(t2)
            if matching_sides:
                while (matching_sides[0]-matching_sides[1])==0 or (matching_sides[0]-matching_sides[1])%2!=0:
                    t2.rotate_right()
                    matching_sides=self.is_adjacent(t2)
                adjacent.append(t2)
        return adjacent

    def get_adjacent_right(self, tiles):
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

    def get_adjacent_down(self, tiles):
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
        self.matrix=np.flipud(self.matrix)
        self.sides[0], self.sides[2]=self.sides[2], self.sides[0]
        self.sides[1].reverse()
        self.sides[3].reverse()
    
    def flip_vertical_axis(self):
        self.matrix=np.fliplr(self.matrix)
        self.sides[1], self.sides[3]=self.sides[3], self.sides[1]
        self.sides[0].reverse()
        self.sides[2].reverse()