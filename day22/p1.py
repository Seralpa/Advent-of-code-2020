with open('day22/input.txt') as f:
    player1, player2=[[int(card) for card in l.splitlines()] for l in f.read().replace('Player 1:\n', '').split('\n\nPlayer 2:\n')]
while len(player1)!=0 and len(player2)!=0:
    c1=player1.pop(0)
    c2=player2.pop(0)
    if c1>c2:
        player1+=c1,c2
    else:
        player2+=c2,c1
winner=player1 if len(player1)!=0 else player2
print(sum([(i+1)*card for i, card in enumerate(reversed(winner))]))