class Day22_1:
    input = """Player 1:
48
23
9
34
37
36
40
26
49
7
12
20
6
45
14
42
18
31
39
47
44
15
43
10
35

Player 2:
13
19
21
32
27
16
11
29
41
46
33
1
30
22
38
5
17
4
50
2
3
28
8
25
24"""

    def __init__(self):
        player1, player2 = self.input.split('\n\n')
        player1 = list(map(int, player1.split('\n')[1:]))
        player2 = list(map(int, player2.split('\n')[1:]))

        while len(player1) > 0 and len(player2) > 0:
            card1 = player1.pop(0)
            card2 = player2.pop(0)
            if card1 > card2:
                player1.append(card1)
                player1.append(card2)
            elif card2 > card1:
                player2.append(card2)
                player2.append(card1)

        winner_deck = max(player1, player2)
        score = 0
        for i, card in enumerate(winner_deck):
            score += card * (len(winner_deck) - i)
        print(score)


Day22_1()
