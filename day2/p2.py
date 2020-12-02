with open("day2/input.txt") as f:
    data=[p.split(' ') for p in f.readlines()]
for p in data:
    p[0]=list(map(int, p[0].split('-')))
    p[1].strip(':')
count=0
for p in data:
    if (p[2][p[0][0]-1]==p[1]) ^ (p[2][p[0][1]-1]==p[1]):
        count+=1
print(count)