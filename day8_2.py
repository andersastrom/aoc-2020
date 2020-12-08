class Day8_2:
    input = """"""

    def __init__(self):
        acc = 0
        original_instructions = self.input.split('\n')
        nr_of_instructions = len(original_instructions)
        visited_indexes = set()
        tested_instructions = set()
        i = 0
        insts = original_instructions
        while True:
            if i == nr_of_instructions:
                print(acc)
                break

            if i in visited_indexes:
                insts, tested_instructions = self.swap(original_instructions.copy(), tested_instructions)
                acc = 0
                visited_indexes = set()
                i = 0

            current_instruction = insts[i]
            inst, nr = current_instruction.split(' ')
            if inst == "acc":
                acc += int(nr)
                visited_indexes.add(i)
                i += 1
            elif inst == "nop":
                visited_indexes.add(i)
                i += 1
            elif inst == "jmp":
                visited_indexes.add(i)
                i += int(nr)

    def swap(self, insts, tested_instructions):
        for i, inst in enumerate(insts):
            if i in tested_instructions:
                continue

            if inst.split(' ')[0] == "nop":
                inst = inst.replace("nop", "jmp")
                insts[i] = inst
                tested_instructions.add(i)
                return insts, tested_instructions
            elif inst.split(' ')[0] == "jmp":
                inst = inst.replace("jmp", "nop")
                insts[i] = inst
                tested_instructions.add(i)
                return insts, tested_instructions


Day8_2()
