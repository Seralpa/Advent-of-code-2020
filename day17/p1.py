def check_neighbours(cube, pos):
    neigbours=0
    for i in range(pos[0]-1, pos[0]+2):
        for j in range(pos[1]-1, pos[1]+2):
            for k in range(pos[2]-1, pos[2]+2):
                if not((i==pos[0] and j==pos[1] and k==pos[2]) or i<0 or i>=len(cube) or j<0 or j>=len(cube[i]) or k<0 or k>=len(cube[i][j])):
                    if cube[i][j][k]=='#':
                        neigbours+=1
    return neigbours

def pretty_print(cube):
    for mat in cube:
        for l in mat:
            for c in l:
                print(c, end='')
            print()
        print()

n=6
with open('day17/input.txt') as f:
    cube=[[list(l) for l in f.read().splitlines()]]

for mat in cube:
    for l in mat:
        for _ in range(n):
            l.insert(0, '.')
            l.append('.')

for mat in cube:
    for _ in range(n):
        mat.insert(0, ['.' for _ in range(len(mat[0]))])
        mat.append(['.' for _ in range(len(mat[0]))])

for _ in range(n):
    cube.insert(0, [['.' for _ in range(len(cube[0][0]))] for _ in range(len(cube[0]))])
    cube.append([['.' for _ in range(len(cube[0][0]))] for _ in range(len(cube[0]))])

for _ in range(n):
    update=[]
    for i in range((len(cube))):
        for j in range((len(cube[i]))):
            for k in range((len(cube[i][j]))):
                neigbours=check_neighbours(cube, (i,j,k))
                if (cube[i][j][k]=='#' and neigbours!=2 and neigbours!=3) or (cube[i][j][k]=='.' and neigbours==3):
                    update.append((i,j,k))
    for pos in update:
        cube[pos[0]][pos[1]][pos[2]]='#' if cube[pos[0]][pos[1]][pos[2]]=='.' else '.'
count=0
for mat in cube:
    for l in mat:
        count+=l.count('#')
print(count)