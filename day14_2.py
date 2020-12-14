import re
import itertools


class Day14_2:
    input = """"""

    def __init__(self):
        instructions = self.input.split('\n')
        mem = {}
        mask = ''
        address = None
        for inst in instructions:
            type, val = inst.split(' = ')
            if type == 'mask':
                mask = val
            elif 'mem' in type:
                as_binary_string = lambda x, n: format(x, 'b').zfill(n)
                value = int(val)
                address = type[4::]
                address = int(address[:-1])
                address_binary = list(as_binary_string(address, 36))
                for index, bit in enumerate(list(mask)[::-1]):
                    if bit == '1':
                        address_binary[len(address_binary) - index - 1] = '1'
                        address = ''.join(address_binary)
                    elif bit == 'X':
                        address_binary[len(address_binary) - index - 1] = 'X'
                        address = ''.join(address_binary)
                self.update_memory(address, mem, value)
        print(sum(mem[key] for key in mem))

    def update_memory(self, address, mem, value):
        sources = re.findall("X", address)
        substitutions = []
        for source in sources:
            substitutions.append(['1', '0'])

        for combination in itertools.product(*substitutions):
            output = address
            for c in combination:
                for index, bit in enumerate(output):
                    if bit == 'X':
                        output = output[:index] + c + output[index + 1:]
                        break
            mem[int(output, 2)] = value


Day14_2()
