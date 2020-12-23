class Day23_2:

    def __init__(self):
        input = "789465123"
        order = {}
        order_set = set()
        for i in range(len(input)):
            nr = int(input[i])
            order_set.add(nr)
            if i == (len(input) - 1):
                order[nr] = 10
                break
            order[nr] = int(input[i + 1])

        for i in range(10, 1000000):
            order[i] = (i + 1)
            order_set.add(i)

        cur = int(input[0])
        order[1000000] = cur
        order_set.add(1000000)

        max_n = max(order_set)
        min_n = min(order_set)

        for i in range(10000000):
            picked_up = []
            for _ in range(3):
                next = order[cur]
                picked_up.append(next)
                order[cur] = order[next]
                del order[next]

            dest = cur - 1
            while dest in picked_up or dest not in order_set:
                dest -= 1
                if dest < min_n:
                    dest = max_n

            next = order[dest]
            picked_cup1 = picked_up.pop(0)
            order[dest] = picked_cup1
            picked_cup2 = picked_up.pop(0)
            order[picked_cup1] = picked_cup2
            picked_cup3 = picked_up.pop(0)
            order[picked_cup2] = picked_cup3
            order[picked_cup3] = next

            cur = order[cur]
        print(order[1] * order[order[1]])


Day23_2()
