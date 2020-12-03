slopes=[[1,1],[3,1],[5,1],[7,1],[1,2]] #col, row
with open("day3/input.txt") as f:
    matrix= [list(l.strip()) for l in f.readlines()]
solution=1
for slope in slopes:    
    row, col, treeCount = 0, 0, 0
    while row<len(matrix):
        treeCount+= 1 if matrix[row][col]=='#' else 0
        if col>=len(matrix[0])-slope[0]:
            for r in matrix:
                r.extend(r)
        row+=slope[1]
        col+=slope[0]
    solution*=treeCount
print(solution)