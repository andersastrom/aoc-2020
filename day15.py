class Day15:
    input = """5,2,8,16,18,0,1"""

    def __init__(self):
        nrs = list(map(int, self.input.split(',')))
        turn = 1
        spoken = {}
        for nr in nrs:
            spoken[nr] = (turn, turn)
            last_spoken = nr
            turn += 1

        for i in range(turn, 30000000 + 1):  # for i in range(turn, 2020 + 1):
            last_spoken = spoken[last_spoken][0] - spoken[last_spoken][1]
            if last_spoken in spoken:
                last_turn = spoken[last_spoken][0]
            else:
                last_turn = turn
            spoken[last_spoken] = (turn, last_turn)
            turn += 1
        print(last_spoken)


Day15()
