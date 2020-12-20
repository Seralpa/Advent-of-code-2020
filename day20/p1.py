class Tile:
    def __init__(self, id_, matrix):
        self.id=id_
        self.matrix=matrix
    
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
        
        for s1 in self.get_sides():
            for s2 in other.get_sides():
                if s1==s2 or list(reversed(s1))==s2:
                    return True

        return False



with open('day20/input.txt') as f:
    data=[d.splitlines() for d in f.read().split('\n\n')]
tiles=[]
for d in data:
    id_=d.pop(0)
    tiles.append(Tile(int(id_[5:-1]), d))
corner_prod=1
for t1 in tiles:
    count=0
    for t2 in tiles:
        if t1.is_adjacent(t2):
            count+=1
    if count==2:
        corner_prod*=t1.id
        print(t1.id)
print(corner_prod)