with open("day3/input.txt") as f:
    matrix= [list(l.strip()) for l in f.readlines()]
row, col, treeCount = 0, 0, 0
slope=(3,1) #col row
while row<len(matrix):
    treeCount+= 1 if matrix[row][col]=='#' else 0
    row+=slope[1]
    col=(col + slope[0]) % len(matrix[0])
print(treeCount)