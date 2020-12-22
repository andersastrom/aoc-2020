class Day17_2:
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
        size = 26
        for i, _ in enumerate(grid):
            a = list(grid[i])
            a.insert(0, "." * int(size / 2 - 8))
            a.append("." * int(size / 2 - 8))
            grid[i] = ''.join(a)

        for i in range(int(size / 2 - 8)):
            grid.insert(0, "." * size)
            grid.append("." * size)

        padding = ["." * size for i in range(size)]
        space = [[padding] * 3, [padding, grid, padding], [padding] * 3]

        for i in range(6):
            new_space = []
            for w_i, w_plane in enumerate(space):
                new_w = []
                for z_i, z_plane in enumerate(w_plane):
                    new_z = z_plane.copy()
                    for y_i, y_plane in enumerate(z_plane):
                        for x_i, x in enumerate(y_plane):
                            adjacent_active = self.count_adjacent_active(x_i, y_i, z_i, w_i, space)
                            if x == '#':
                                if adjacent_active < 2 or adjacent_active > 3:
                                    new_z[y_i] = new_z[y_i][:x_i] + '.' + new_z[y_i][x_i + 1:]
                            elif x == '.':
                                if adjacent_active == 3:
                                    new_z[y_i] = new_z[y_i][:x_i] + '#' + new_z[y_i][x_i + 1:]

                    new_w.append(new_z)
                new_w.insert(0, padding)
                new_w.append(padding)
                new_space.append(new_w)
            new_space.insert(0, [padding for _ in range(5 + i * 2)])
            new_space.append([padding for _ in range(5 + i * 2)])
            space = new_space

        count = 0
        for w in space:
            for z in w:
                for y in z:
                    count += y.count('#')
        print(count)

    def count_adjacent_active(self, x_i, y_i, z_i, w_i, grid):
        adjacent_active = 0
        dirs = {-1, 0, 1}
        for w in [w_i + d for d in dirs]:
            for z in [z_i + d for d in dirs]:
                for y in [y_i + d for d in dirs]:
                    for x in [x_i + d for d in dirs]:
                        try:
                            if (grid[w][z][y][x] == '#') and not (w == w_i and z == z_i and y == y_i and x == x_i):
                                adjacent_active += 1
                        except Exception:
                            pass
        return adjacent_active


Day17_2()
