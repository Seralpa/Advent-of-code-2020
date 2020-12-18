def check_neighbours(hypercube, pos):
    neigbours=0
    for i in range(pos[0]-1, pos[0]+2):
        for j in range(pos[1]-1, pos[1]+2):
            for k in range(pos[2]-1, pos[2]+2):
                for w in range(pos[3]-1, pos[3]+2):
                    if not((i==pos[0] and j==pos[1] and k==pos[2] and w==pos[3]) or i<0 or i>=len(hypercube) or j<0 or j>=len(hypercube[i]) or k<0 or k>=len(hypercube[i][j]) or w<0 or w>=len(hypercube[i][j][k])):
                        if hypercube[i][j][k][w]=='#':
                            neigbours+=1
    return neigbours

def pretty_print(hypercube):
    for cube in hypercube:
        for mat in cube:
            for l in mat:
                for c in l:
                    print(c, end='')
                print()
            print()
        print()

n=6
with open('day17/input.txt') as f:
    hypercube=[[[list(l) for l in f.read().splitlines()]]]
for cube in hypercube:
    for mat in cube:
        for l in mat:
            for _ in range(n):
                l.insert(0, '.')
                l.append('.')

for cube in hypercube:
    for mat in cube:
        for _ in range(n):
            mat.insert(0, ['.' for _ in range(len(mat[0]))])
            mat.append(['.' for _ in range(len(mat[0]))])

for cube in hypercube:
    for _ in range(n):
        cube.insert(0, [['.' for _ in range(len(hypercube[0][0][0]))] for _ in range(len(hypercube[0][0]))])
        cube.append([['.' for _ in range(len(hypercube[0][0][0]))] for _ in range(len(hypercube[0][0]))])

for _ in range(n):
    hypercube.insert(0, [[['.' for _ in range(len(hypercube[0][0][0]))] for _ in range(len(hypercube[0][0]))] for _ in range(len(hypercube[0]))])
    hypercube.append([[['.' for _ in range(len(hypercube[0][0][0]))] for _ in range(len(hypercube[0][0]))] for _ in range(len(hypercube[0]))])

for cycle in range(n):
    print(f"{cycle}/{n}")
    update=[]
    for i in range((len(hypercube))):
        for j in range((len(hypercube[i]))):
            for k in range((len(hypercube[i][j]))):
                for w in range(len(hypercube[i][j][k])):
                    neigbours=check_neighbours(hypercube, (i,j,k,w))
                    if (hypercube[i][j][k][w]=='#' and neigbours!=2 and neigbours!=3) or (hypercube[i][j][k][w]=='.' and neigbours==3):
                        update.append((i,j,k,w))
    for pos in update:
        hypercube[pos[0]][pos[1]][pos[2]][pos[3]]='#' if hypercube[pos[0]][pos[1]][pos[2]][pos[3]]=='.' else '.'
count=0
for cube in hypercube:
    for mat in cube:
        for l in mat:
            count+=l.count('#')
print(count)