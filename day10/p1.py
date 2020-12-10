with open('day10/input.txt') as f:
    data=[int(l) for l in f]
data.append(0)
data.sort()
diffs=[data[i+1]-data[i] for i in range(len(data)-1)]
print(diffs.count(1)*(diffs.count(3)+1))    #+1 cause target joltage is 3 above max