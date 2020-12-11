class Day11_2:
    input = """"""

    nr_of_seats = 98
    nr_of_rows = 97

    def __init__(self):
        layout = self.input.split('\n')
        while True:
            new_layout = []
            for row_nr, row in enumerate(layout):
                new_row = ""
                for seat_nr, seat in enumerate(row):
                    if seat == 'L' or seat == '#':
                        count = self.count_adjacent_occupied_seats(seat_nr, row_nr, layout)
                        if seat == 'L' and count == 0:
                            new_row = new_row + '#'
                        elif seat == '#' and count >= 5:
                            new_row = new_row + 'L'
                        else:
                            new_row = new_row + seat
                    else:
                        new_row = new_row + seat
                new_layout.append(new_row)

            if new_layout == layout:
                occurrences = 0
                for r in new_layout:
                    occurrences += r.count('#')
                print(occurrences)
                return
            layout = new_layout

    def count_adjacent_occupied_seats(self, x, y, layout):
        sum = 0
        adjacent_indexes = []
        directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        for direction in directions:
            adjacent_seat = '.'
            x_index = x
            y_index = y
            while adjacent_seat == '.':
                if self.is_adjacent_index(direction, x_index, y_index):
                    x_index = x_index + direction[0]
                    y_index = y_index + direction[1]
                    adjacent_seat = layout[y_index][x_index]
                    if adjacent_seat == '#' or adjacent_seat == 'L':
                        adjacent_indexes.append((x_index, y_index))
                else:
                    adjacent_seat = None

        for i in adjacent_indexes:
            if layout[i[1]][i[0]] == '#':
                sum += 1
        return sum

    def is_adjacent_index(self, direction, x_index, y_index):
        adjacent_x = ((direction[0] + x_index) % self.nr_of_seats)
        adjacent_y = ((direction[1] + y_index) % self.nr_of_rows)
        diff_x = abs(adjacent_x - x_index)
        diff_y = abs(adjacent_y - y_index)
        return (diff_x == 1 or diff_x == 0) and (diff_y == 1 or diff_y == 0)


Day11_2()
