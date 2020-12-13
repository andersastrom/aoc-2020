class Day13_2:
    input = """1000052
23,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,863,x,x,x,x,x,x,x,x,x,x,x,19,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,571,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41"""

    def __init__(self):
        timestamp, ids = self.input.split('\n')
        timestamp = int(timestamp)
        ids = list(map(int, ids.replace('x', '0').split(',')))

        buses = [(i, index) for index, i in enumerate(ids) if i is not 0]
        step = buses[0][0]
        timestamps = [0]
        for bus_index, bus in enumerate(buses[1::]):
            bus_id = bus[0]
            bus_time_offset = bus[1]
            timestamp_range = step * bus_id
            timestamp_candidates = [i for i in range(timestamps[bus_index], timestamp_range, step)]
            for index, timestamp_candidate in enumerate(timestamp_candidates):
                if ((timestamp_candidate + bus_time_offset) % bus_id) == 0:
                    timestamps.append(timestamp_candidate)
                    step = timestamp_range
        print(timestamps[-1])


Day13_2()
