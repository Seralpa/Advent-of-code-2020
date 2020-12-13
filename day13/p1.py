with open('day13/input.txt') as f:
    initial_timestamp=int(f.readline())
    ids=[int(bus) for bus in f.readline().strip().split(',') if bus!='x']
earliest=initial_timestamp
while True:
    for bus in ids:
        if earliest%bus==0:
            print((earliest-initial_timestamp)*bus)
            raise SystemExit
    earliest+=1