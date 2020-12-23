cups=list('123487596')  #input
# cups=list('389125467')  #test
cups=list(map(int, cups))
current=cups[0]
for i in range(100):
    current_index=cups.index(current)
    pick_up=[cups.pop((current_index+1)if (current_index+1)<len(cups) else 0) for _ in range(3)]
    destination=current-1
    while destination not in cups:
        destination=(destination-1)%10
    destination_index=cups.index(destination)
    for c in reversed(pick_up):
        cups.insert(destination_index+1, c)
    current=cups[(cups.index(current)+1)%len(cups)]
print(cups)