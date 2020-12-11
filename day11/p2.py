def check_adjacent(data, pos):
    occupied=0
    i=0
    while pos[0]-i>0:
        i+=1
        if data[pos[0]-i][pos[1]]=='#':
            occupied+=1
            break
        elif data[pos[0]-i][pos[1]]=='L':
            break

    i=0
    while pos[0]+i<len(data)-1:
        i+=1
        if data[pos[0]+i][pos[1]]=='#':
            occupied+=1
            break
        elif data[pos[0]+i][pos[1]]=='L':
            break

    i=0
    while pos[1]-i>0:
        i+=1
        if data[pos[0]][pos[1]-i]=='#':
            occupied+=1
            break
        elif data[pos[0]][pos[1]-i]=='L':
            break

    i=0
    while pos[1]+i<len(data[0])-1:
        i+=1
        if data[pos[0]][pos[1]+i]=='#':
            occupied+=1
            break
        elif data[pos[0]][pos[1]+i]=='L':
            break

    i=0
    while pos[0]-i>0 and pos[1]-i>0:
        i+=1
        if data[pos[0]-i][pos[1]-i]=='#':
            occupied+=1
            break
        elif data[pos[0]-i][pos[1]-i]=='L':
            break

    i=0
    while pos[0]-i>0 and pos[1]+i<len(data[0])-1:
        i+=1
        if data[pos[0]-i][pos[1]+i]=='#':
            occupied+=1
            break
        elif data[pos[0]-i][pos[1]+i]=='L':
            break

    i=0
    while pos[0]+i<len(data)-1 and pos[1]-i>0:
        i+=1
        if data[pos[0]+i][pos[1]-i]=='#':
            occupied+=1
            break
        elif data[pos[0]+i][pos[1]-i]=='L':
            break

    i=0
    while pos[0]+i<len(data)-1 and pos[1]+i<len(data[0])-1:
        i+=1
        if data[pos[0]+i][pos[1]+i]=='#':
            occupied+=1
            break
        elif data[pos[0]+i][pos[1]+i]=='L':
            break
    return occupied

def pretty_print(data):
    for row in data:
        print()
        for seat in row:
            print(seat, end=' ')
    print()

with open('day11/input.txt') as f:
    data=[list(l) for l in f.read().splitlines()]
seatnum=0
while True:
    prevseatnum=seatnum
    seatnum=0
    update=[]
    for i in range(len(data)):
        for j in range(len(data[0])):
            occupied=check_adjacent(data, (i, j))
            if (data[i][j]=='L' and occupied==0) or (data[i][j]=='#' and occupied>=5):
                update.append((i,j))
    for u in update:
        data[u[0]][u[1]]='#' if data[u[0]][u[1]]=='L' else 'L'
    for row in data:
        seatnum+=row.count('#')
    # pretty_print(data)
    if seatnum==prevseatnum:
        print(seatnum)
        break