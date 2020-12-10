class Day10_1:
    input = """"""

    def __init__(self):
        adapters = list(map(int, self.input.split('\n')))
        ones = 0
        threes = 1
        current = 0
        for a in adapters:
            if (current + 1) in adapters:
                current += 1
                ones += 1
            elif (current + 2) in adapters:
                current += 2
            elif (current + 3) in adapters:
                current += 3
                threes += 1
        print(ones * threes)


Day10_1()
