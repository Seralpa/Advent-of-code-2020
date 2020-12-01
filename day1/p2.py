with open("day1/input.txt") as f:
    l=list(map(int, f.readlines()))
    for i in l:
        for j in l:
            for k in l:
                if (i+j+k)==2020:
                    print(i*j*k)
                    raise SystemExit()