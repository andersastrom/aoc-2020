class Day23_1:

    def __init__(self):
        input = "789465123"
        order = list(map(int, input))
        nr_of_cups = len(order)
        cur = order[0]

        for i in range(100):
            picked_up = []
            [picked_up.append(order.pop((order.index(cur) + 1) % (nr_of_cups - p))) for p in range(3)]
            dest = cur - 1
            while dest in picked_up or dest not in order:
                dest -= 1
                if dest < min(order):
                    dest = max(order)
            for cup_i, cup in enumerate(order):
                if cup == dest:
                    [order.insert(cup_i + 1, picked_up.pop()) for x in range(3)]
                    break

            cur = order[(order.index(cur) + 1) % nr_of_cups]

        one_i = order.index(1)
        order.pop(one_i)
        print(''.join([str(order[(one_i + i) % len(order)]) for i in range(len(order))]))


Day23_1()
