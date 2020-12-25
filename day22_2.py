class Day22_2:
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

        winner_deck = self.play_game(player1, player2)
        score = 0
        for i, card in enumerate(winner_deck[1]):
            score += card * (len(winner_deck[1]) - i)
        print(score)

    def play_game(self, player1, player2):
        player1_played_sets = set()
        player2_played_sets = set()
        while len(player1) > 0 and len(player2) > 0:
            if tuple(player1) in player1_played_sets or tuple(player2) in player2_played_sets:
                return (1, player1)

            player1_played_sets.add(tuple(player1.copy()))
            player2_played_sets.add(tuple(player2.copy()))

            card1 = player1.pop(0)
            card2 = player2.pop(0)

            if len(player1) >= card1 and len(player2) >= card2:
                winner = self.play_game(player1.copy()[0:card1], player2.copy()[0:card2])
                if winner[0] == 1:
                    player1.append(card1)
                    player1.append(card2)
                elif winner[0] == 2:
                    player2.append(card2)
                    player2.append(card1)
            else:
                if card1 > card2:
                    player1.append(card1)
                    player1.append(card2)
                elif card2 > card1:
                    player2.append(card2)
                    player2.append(card1)

        winner = max(player1, player2)
        if winner == player1:
            return (1, player1)
        else:
            return (2, player2)


Day22_2()
