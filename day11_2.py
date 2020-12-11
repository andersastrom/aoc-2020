class Day11_2:
    input = """LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL..LLLLLLLLLLLL.LLL..LLLLLLLLLLLLLL.LL.LLLLL.LLLLLLLLL.LLLLLLLLLLLLL
LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLL.LLLL.LLLLLLLL.LLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLL..LLLLLLL..LLLL
LLLLLL.LLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLL.LLL.LLLLLLLLLLLLLL.LLLLLLL..LLLLLLLLLLLLLLLLLLLLLL.LLLLL
LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL..LLLLLLLLL.LLLLLLL..LLLL
.LLL.LL.LLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLL.LLLLLLLLLLLLL
LL.LLLL.LLLLLLLLLLLLLLLLL.LLLLL.LLLL.LLLLLLLLLLLLL.LLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLL.LLLLL
......L........LLL....L.L......L.LL...L.....L.LL..L..L..L..LLL..LL......L...L.LL.L.L....L.........
LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLL.LLLLLLLLL.LLL.LLLLLLLLL.L.LLLLL.LLLLL.LLLLLLLLL.LLLLLLL.LLLLL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLLLLL.LLLLL
LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLL.LLLL.LLLLLLLL.LLLL.LLLLLL.LL.LLLLLLL.LLLLLLLLLLLLLLL.LLLLLLL.LLLLL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLL.LLLL..LLLLLLL.LLLLLLLLLLLLLL.LLL.LLL..LLLL.LLLLLLLLL.LLLLLLL.LLLLL
LLLLLLL.LLL.LLLLLLL.LLLLL.LLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLLLLLLL.LLLL.L.LLL.LLLLLLLLLLLLLLLLL.LLLLL
LLLLL.L.LLLLLLL.LLLLLL.LL.LLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLLLL.L.L..LLLLLLL.LLLLLLLLLL.LLLLLLLLLLLLL
.L....LLLL.LL.LL..L.L.L.L.LL..L..L.LLLLLL.L.LLLL.L.L..LL...L..L..LLL.....L........LL.L..L..L..L..L
LLLLLLL.LLLLLLL.LLLLL.LLL.LLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLL..LLLLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLL
LLLLLLL.LL.LLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLL
LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLLL.LLL.L
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLL.LL.LLLLL
.....L..L...L.L.L..........L..LLLL....L..L.L..LLLL...L..L....L.LL.L....L.L.L....LL.L..L......LLL.L
LLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLL.LL.LLLLLL.LL.LLLL.LLLLL
LLLLLLL.L.LLLLLLLLLL.LLLL.L.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLL
LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLL.LLLLL
LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLL.L.LL.LLLLLLLLLLLLL.LLLLLLLLL.LLLL.LLLLLLLLLLLLLLL.L..LLLLLLLLLLL.L
LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLL.LLLLLL.L.LLLL.L.LLLLLLLLLLLLLLL.LLLLLLLLLLLLL.L.LLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLL.LL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLL.LLLLLLL.LLLLL
LLLLLLL.LL.LLLLLLLL.LLLLL.LLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.L.LLLLLLL.LLLLL
L.LLLLL.LLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLL.LLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLL
..L...L...L......L.LLLL.....LLL.L.LLLLLL.L.L.L..L.L.......L.L..L...L.L.L....LL...L.LL......LL.L.L.
LLLLLLL.LLLLLLL.L.LLLLLLL.LLLLL.LLL.LLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLL.LLLLLLL.LLLLL
LLLLLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLL..LLL.LLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLLL.LLLLL
LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLL.LLL.L.LLLLL.LLLLLLLLLLL.LLLLL
LLLLLLL.LLLLLLL.LL.LLLLLL..LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL..LLLLLLLL.LLLL.LL.LLLLL
LL.LLLL.LLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.L.LLLLL.LLLLLLLLLLLLLLLLLLLLLLL.L.LLLLLLL.LLLLL
LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLL.LLLL.LLLLLLLL.LLLL.LLLLLL.LL.LLLLL.L.LLLLL.LLLLLLLLLLLLLLLLLLLLLLL
LLLLLLL.LLL.LLL.LLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLL.LLLLL
L.L.......L.L....LL......LL.LL...LL..L...........L.....LLL....L..LL.LL.L.L.LL.......L.L...L....L..
LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLL.LLLL.LLLLLLLLLLLLL.LLLLLLLLL.LLLLLLL.LL.LL.LLLLLLLLLLLLLLLLL.LLL.L
LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLL.LL.LLLLLLLLLL.LL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL
LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLL.LLLL..LLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.L..LL.LLL.LLLLLLLLLLLLLLLLLLL
LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLL.LLLLL
LLLLLLLLLL.LLLL.LLLLLLL.LLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL
L.LLLLLLLLLLLLL.LL.LLLLLL.LLLLL.LLLL.LLLLLLLL.LLLLLLLLLLL.LL.LLLL.LLLLLLLLLL.LLLLLLL.LLLLLLL.LLLLL
...LL.L..LL...L.......L.LL.......LL.LLL.L.LLL...L..LLL.L...L.......LL.LL.LL.L..LL........L.......L
LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLLLLL.LLLLL
LLLLLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLLLLLLL.LLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLL
LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLL.LLLLL.L..LLLL.LLLLLLLLL.LLLL.LLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLL..LLLLLLLLLLLLLLL..LL.LL.L.LLL.LLL.LLLLLLL.LLLLL
LLLLL..LLLL.LLLLLLLLLLLLL.LLLLLLLL.L.LLLLLLLL.LLLL.LLLLLLLLL.L.LLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLL.L.LLLLLLLLL.LLLLL.L.LLLLL
.LLLLLL.LLLLLLL..LLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLL.LLLLL
LLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLL
..LL....L..........LL..L....L.LL...L.L...L.L...LLL..LL....LL.L.L.LLLL...L.L.......L.....LL........
LLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LL.L.
LLLLLLL.LLLL.LL.LLL.LLLLL.LLLLL.LLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LL.LLLLLLL.LL
LL.LLLLLLLLLL.LLLLLLLLLLL.LLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLLLL.LLL.LLL.LLLLL.LLLLLLLLL.LLLLLLL.LLLLL
LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLL.LLLLLLL.LLLL.
LLLLLLLLLLLLLLL.LLLLLLLL.LLLLLL.LLLL.LLLLLLLLLLLLL.LLLLLLLLL.LLL.LLL.L.LLLLLLLLLLLLLLLLLLLLL.LLLLL
LLLLLLL.LLLLLLL.LLLLLLL.L.LLLLL.LLLL.LLLL.LLL.LLLLLLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLLL.LLL.L
LLLLLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLL.L.LLLLLLLLLLL.LLLLLLLLL.LL.LLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLL
LLL.LLL.L.LLLLL.LLLLLLLLL.LLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLL.L.LLLLLLLLL.LLL.LLLLLLLLLLLLLLLLLLLLLLL
..LLL.LL.....LL...LL..L..LLL...........LL...........L.....L.......L..LLLLL......L......LL..L...L.L
LLLLLLL.LLLLLLL.L.LLLLLLLLLL.LL.LLLL.LLLLLLLLLLLLL.LLLLLLL.L.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL
LLLLLLLLLLLLLLL.LL..LL.LLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLL.LLL.LLL.LLLLL
LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLL..LLLL.LLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLLL.LLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLL
LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLL.LLLL.LL.LLLLL.LLLL.LLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLLL.LLLLLLL.L.LLL
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLL..LLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLL.LLLLLLL..LLLL
LLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLL.LL.LLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLLLL.LLLLLLL.LLLL..LLLLLLLLLLLLLLLLL.LLLLL
.......L...LLL.L....L.LL......L.L...L...LL.LL...L...L..L.L.LL.........L.L..L.L.L.......L..L.....L.
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLL.LLLLLLL..LLLLLLLLLLLLL..LLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLL.LLLL.LLLLLLLLLLLLL.LLLLLLLLL.LL.LLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLL
LLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LL.LLLLLLLLLLLLLLLLL.L.LLLLL.LLLLLLLLL.LLLLLLL.LLLLL
LLLLLLL.LLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLL.LLLLL.LLL.LLLLLLLLLLLLL.L.LLLLLLL.LLLLLLLLLLLLL
LLLLLLL.LLL.LLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLLLLL.LLLLL
LLLLLL..LL.LLLLL.LLLLLLLL.L.LLL.LLLL.LLLLLLLLLLLLLLLL..LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
.LLLL.L.LLLLLLL.LLLLLLLLL.LLLLLLLLLL..LLL.LLL.LLLL.LLLLLLLLL.LLLL.LL.LLLLL.LLLLLLLLL.LLLLLLL..L.LL
LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL..LL.LLLLLLLLLL.LL.LLLLLL.LLLLL.L.LLLLL.LLLLLL..LLLLLLLLL.LLLLL
..L...L..L..L.L..LL.L.LLL.LLL.L....L..LL.....L....LL...L.L.L.L...L.L.....LLL......L...LL.L.......L
LLLLLLLLLLLLLLL.LLLLLLLLL.LLLL.LLLLL.LLLLLLL.LLLLL..LLLLLLLLLLL.L.LL.LLLLLLLLLLLL.LL.LLL.LLL.LLLLL
LLLLLLL.LLLLLL..LLLLLLLLL.LLLLLLLLLL.LLLLLLLL.LLLL.LLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLLLLL.LLLLL
LLLLLLL..LLLLLL.LLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLL.LLLLLLL.L.LLL
LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLL.LLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLL.LL.LLLLL
..L..LL.L.L...LL...L.LL.LL....L.L.L.LLL...LL.LL...L...L...LLLLLL.LLL...L.L.LL................LL.L.
LLLLLLLLLLL.LLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLL.LLLLLLLLLL.LLLLLLL.LLLLLLLLLL.LLLL.LLLLLLLLLLLLL
LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLL.LLLLLLLLLLLLL
LLLLLLL.LLLLL.L.LLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLL.LLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLL
LLLLLLL.LLLLLLL.LLLLLLLLL.L.LLL.LL.LLLLLLLL.L.LLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL
.LL.LLL.LLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLLLL.L.LLLLLLLLLLLLLLLLL.LLLLL
LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLL.LLLLLLLL.LL.LLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL
LLLL.LL.LLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLL.LLLLL
LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LL.LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLLLLLLL.LLLLL
LLLLLLL.LLLLLLL..LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLL.LL.LLLL.LLLLL.LLLLLLLLL.LLLLLLL.LLLLL"""

    def __init__(self):
        rows = self.input.split('\n')
        target = None
        while True:
            # cop = rows.copy()
            new_layout = []
            # print(rows)
            for row_nr, row in enumerate(rows):
                new_row = ""
                for seat_nr, seat in enumerate(row):
                    if seat == 'L':
                        target = '#'
                    elif seat == '#':
                        target = '#'
                    else:
                        target = None
                    # print(target)
                    if target:
                        count = self.count(seat_nr, row_nr, row, rows, target)
                        if seat == 'L' and count == 0:
                            # print("here")
                            new_row = new_row + '#'
                        elif seat == '#' and count >= 5:
                            new_row = new_row + 'L'
                        else:
                            new_row = new_row + seat
                    else:
                        new_row = new_row + seat
                new_layout.append(new_row)

            print(new_layout)
            if new_layout == rows:
                print(new_layout)
                occs = 0
                for r in new_layout:
                    occs += r.count('#')
                print(occs)
                return
            rows = new_layout

    def count(self, x, y, row, rows, target):
        nr_of_seats = len(row)
        nr_of_rows = len(rows)
        # print(nr_of_seats)
        # print(nr_of_rows)
        sum = 0
        adjacent_indexes = []
        dir = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        for p in dir:
            diffx, diffy = self.get_dir(p, x, y, nr_of_seats, nr_of_rows)
            if (diffx == 1 or diffx == 0) and (diffy == 1 or diffy == 0):
                new_x = x + p[0]
                new_y = y + p[1]
                look = rows[new_y][new_x]
                if look == '.':
                    while look == '.':
                        diffx, diffy = self.get_dir(p, new_x, new_y, nr_of_seats, nr_of_rows)
                        if (diffx == 1 or diffx == 0) and (diffy == 1 or diffy == 0):
                            new_x = new_x + p[0]
                            new_y = new_y + p[1]
                            look = rows[new_y][new_x]
                            if look == '#' or look == 'L':
                                adjacent_indexes.append((new_x, new_y))
                        else:
                            look = None
                else:
                    adjacent_indexes.append((new_x, new_y))

        for i in adjacent_indexes:
            if rows[i[1]][i[0]] == target:
                sum += 1
        return sum

    def get_dir(self, p, x, y, nr_of_seats, nr_of_rows):
        xt = ((p[0] + x) % nr_of_seats)
        yt = ((p[1] + y) % nr_of_rows)
        diffx = abs(xt - x)
        diffy = abs(yt - y)
        return diffx, diffy


Day11_2()
