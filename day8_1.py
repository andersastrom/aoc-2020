class Day8_1:
    input = """"""

    def __init__(self):
        acc = 0
        instructions = self.input.split('\n')
        visited_indexes = set()
        i = 0
        current_instruction = instructions[i]
        while True:
            if i in visited_indexes:
                print(acc)
                break
            inst, nr = current_instruction.split(' ')
            if inst == "acc":
                acc += int(nr)
                visited_indexes.add(i)
                i += 1
                current_instruction = instructions[i]
            elif inst == "nop":
                visited_indexes.add(i)
                i += 1
                current_instruction = instructions[i]
            elif inst == "jmp":
                visited_indexes.add(i)
                i += int(nr)
                current_instruction = instructions[i]


Day8_1()
