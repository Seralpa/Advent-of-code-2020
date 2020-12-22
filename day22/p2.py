def play_game(player1, player2):
    loop_check=set()
    while len(player1)!=0 and len(player2)!=0:
        if (tuple(player1), tuple(player2)) in loop_check:
            player2=[]
            break
        loop_check.add((tuple(player1), tuple(player2)))
        c1=player1.pop(0)
        c2=player2.pop(0)
        if c1<=len(player1) and c2<=len(player2):
            sub_p1, sub_p2=play_game(player1[:c1], player2[:c2])
            if len(sub_p2)==0:
                player1+=c1,c2
            else:
                player2+=c2,c1
        else:
            if c1>c2:
                player1+=c1,c2
            else:
                player2+=c2,c1
    return player1, player2

with open('day22/input.txt') as f:
    player1, player2=[[int(card) for card in l.splitlines()] for l in f.read().replace('Player 1:\n', '').split('\n\nPlayer 2:\n')]
player1, player2=play_game(player1, player2)
winner=player1 if len(player1)!=0 else player2
print(sum([(i+1)*card for i, card in enumerate(reversed(winner))]))