with open("day1/input.txt") as f:
    l=list(map(int, f.readlines()))
    for i in l:
        for j in l:
            if (i+j)==2020:
                print(i*j)
                raise SystemExit()