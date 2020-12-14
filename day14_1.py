class Day14_1:
    input = """"""

    def __init__(self):
        insts = self.input.split('\n')
        mem = [0 for i in range(66000)]
        mask = ''
        address = None
        for inst in insts:
            typ, val = inst.split(' = ')
            if typ == 'mask':
                mask = val
            elif 'mem' in typ:
                as_binary_string = lambda x, n: format(x, 'b').zfill(n)
                value = int(val)
                address = typ[4::]
                address = int(address[:-1])
                address_binary = list(as_binary_string(value, 36))
                for index, bit in enumerate(list(mask)[::-1]):
                    if bit == '1':
                        address_binary[len(address_binary) - index - 1] = '1'
                        value = int(''.join(address_binary), 2)
                    elif bit == '0':
                        address_binary[len(address_binary) - index - 1] = '0'
                        value = int(''.join(address_binary), 2)
                mem[address] = value
        print(sum(mem))


Day14_1()
