class Day13_1:
    input = """1000052
23,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,863,x,x,x,x,x,x,x,x,x,x,x,19,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,571,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41"""

    def __init__(self):
        timestamp, ids = self.input.split('\n')
        timestamp = int(timestamp)
        ids = list(map(int, ids.replace('x,', '').split(',')))
        buses = [(id, ((timestamp // id) * id + id) - timestamp) for id in ids]
        min_timestamp = min([bus[1] for bus in buses])
        for bus in buses:
            if bus[1] == min_timestamp:
                print(bus[0] * bus[1])


Day13_1()
