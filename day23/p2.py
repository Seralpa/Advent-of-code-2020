class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

    def insert_after(self,new):
        new.prev=self
        new.next=self.next
        self.next.prev=new
        self.next=new

    def pop_next(self):
        next=self.next
        two_forward=self.next.next
        self.next=two_forward
        two_forward.prev=self
        return next

    def __eq__(self, other):
        return self.data==other.data

cups=list('123487596')  #input
# cups=list('389125467')  #test
cups=list(map(int, cups))

nodes=[None for _ in cups]  #index 0 contains node of data 1
prev=None
for c in cups:
    n=Node(c, prev=prev)
    if prev:
        prev.next=n
    nodes[c-1]=n
    prev=n

for i in range(10, 1000001):
    n=Node(i, prev=prev)
    if prev:
        prev.next=n
    nodes.append(n)
    prev=n

nodes[cups[0]-1].prev=nodes[-1]
nodes[-1].next=nodes[cups[0]-1]

current=nodes[cups[0]-1]
for i in range(10000000):
    pick_up=[current.pop_next() for _ in range(3)]
    destination_data=current.data-1
    while destination_data in [d.data for d in pick_up] or destination_data==0:
        destination_data=(destination_data-1)%1000001
    destination=nodes[destination_data-1]
    for c in reversed(pick_up):
        destination.insert_after(c)
    current=current.next
print(nodes[0].next.data * nodes[0].next.next.data)