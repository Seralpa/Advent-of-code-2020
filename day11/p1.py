directions=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
def check_adjacent(data, pos):
    occupied=0
    for d in directions:
        if pos[0]+d[0]>=0 and pos[1]+d[1]>=0 and pos[0]+d[0]<len(data) and pos[1]+d[1]<len(data[0]) and data[pos[0]+d[0]][pos[1]+d[1]]=='#':
            occupied+=1
    return occupied

with open('day11/input.txt') as f:
    data=[list(l) for l in f.read().splitlines()]
seatnum=0
while True:
    prevseatnum=seatnum
    update=[]
    for i in range(len(data)):
        for j in range(len(data[0])):
            occupied=check_adjacent(data, (i, j))
            if (data[i][j]=='L' and occupied==0) or (data[i][j]=='#' and occupied>=4):
                update.append((i,j))
    for u in update:
        data[u[0]][u[1]]='#' if data[u[0]][u[1]]=='L' else 'L'
    seatnum=sum([row.count('#') for row in data])
    if seatnum==prevseatnum:
        print(seatnum)
        break