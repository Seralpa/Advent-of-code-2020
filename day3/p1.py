with open("day3/input.txt") as f:
    matrix= [list(l.strip()) for l in f.readlines()]
row, col, treeCount = 0, 0, 0
slope=(3,1) #col row
while row<len(matrix):
    treeCount+= 1 if matrix[row][col]=='#' else 0
    if col>=len(matrix[0])-slope[0]:
        for r in matrix:
            r.extend(r)
    row+=slope[1]
    col+=slope[0]
print(treeCount)