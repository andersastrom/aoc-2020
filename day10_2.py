class Day10_2:
    input = """"""

    def __init__(self):
        adapters = sorted(list(map(int, self.input.split('\n'))))
        adapters.insert(0, 0)
        adapters.append(max(adapters) + 3)
        combinations_at_index = []
        combinations_at_index.append(1)
        for outer in range(1, len(adapters)):
            combinations = 0
            for inner in range(outer):
                if (adapters[inner] + 3) >= adapters[outer]:
                    combinations += combinations_at_index[inner]
            combinations_at_index.append(combinations)
        print(combinations)


Day10_2()
