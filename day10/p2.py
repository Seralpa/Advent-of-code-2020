known=dict()
def arrangements(data):
    if len(data)<2:
        return 1
    if data in known.keys():
        return known[data]
    else:
        ways=arrangements(data[:-1])
        if len(data)>2 and data[-1]-data[-3]<=3:
            ways+=arrangements(data[:-2])
            if len(data)>3 and data[-1]-data[-4]<=3:
                ways+=arrangements(data[:-3])
        known[data]=ways
        return ways

with open('day10/input.txt') as f:
    data=[int(l) for l in f]
data.append(0)
data.sort()
print(arrangements(tuple(data)))