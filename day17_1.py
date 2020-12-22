class Day17_1:
    input = """#.#.#.##
.####..#
#####.#.
#####..#
#....###
###...##
...#.#.#
#.##..##"""

    def __init__(self):
        grid = self.input.split('\n')
        size = 20
        for i, _ in enumerate(grid):
            a = list(grid[i])
            a.insert(0, "." * int(size / 2 - 8))
            a.append("." * int(size / 2 - 8))
            grid[i] = ''.join(a)

        for i in range(int(size / 2 - 8)):
            grid.insert(0, "." * size)
            grid.append("." * size)

        padding = ["." * size for i in range(size)]
        space = [padding, grid, padding]
        for i in range(6):
            new_space = []
            for z_i, z in enumerate(space):
                new_z = z.copy()
                for y_i, y in enumerate(z):
                    for x_i, x in enumerate(y):
                        adjacent_active = self.count_adjacent_active(x_i, y_i, z_i, space)
                        if x == '#':
                            if adjacent_active < 2 or adjacent_active > 3:
                                new_z[y_i] = new_z[y_i][:x_i] + '.' + new_z[y_i][x_i + 1:]
                        elif x == '.':
                            if adjacent_active == 3:
                                new_z[y_i] = new_z[y_i][:x_i] + '#' + new_z[y_i][x_i + 1:]

                new_space.append(new_z)
            new_space.insert(0, padding)
            new_space.append(padding)
            space = new_space

        count = 0
        for z in new_space:
            for y in z:
                count += y.count('#')
        print(count)

    def count_adjacent_active(self, x_i, y_i, z_i, space):
        adjacent_active = 0
        dirs = {-1, 0, 1}
        for z in [z_i + d for d in dirs]:
            for y in [y_i + d for d in dirs]:
                for x in [x_i + d for d in dirs]:
                    try:
                        if (space[z][y][x] == '#') and not (z == z_i and y == y_i and x == x_i):
                            adjacent_active += 1
                    except Exception:
                        pass
        return adjacent_active


Day17_1()
