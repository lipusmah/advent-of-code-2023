import copy

def get_grid(lines):
    grid = []
    for i, l in enumerate(lines):
        line = l.strip()
        row = []
        for j, char in enumerate(line):
            if char == "#":
                row.append(1)
            else:
                row.append(0)
        grid.append(row)
    return grid

def get_empty_rows_index(grid):
    empty = []
    for i, row in enumerate(grid):
        if all([r == 0 for r in row]):
            empty.append(i)

    return empty

def get_empty_columns_index(grid):
    empty = []
    for i in range(len(grid[0])):
        if all([row[i] == 0 for row in grid]):
            empty.append(i)

    return empty

def get_coords(grid):
    coords = []
    for i, _ in enumerate(grid):
        for j, val in enumerate(grid[i]):
            if val == 1:
                coords.append((len(coords)+1, (i, j)))
                
    return coords

def get_manhattan(c1, c2):
    x = abs(c1[0] - c2[0])
    y = abs(c1[1] - c2[1])
    return  x + y

def get_bellow_count(item_list, item):
    c = 0
    for i in item_list:
        if i < item:
            c+= 1
        else:
            return c
    return c


if __name__ == "__main__":
    with open("input.txt") as f:
        grid = get_grid(f.readlines())
        empty_rows = get_empty_rows_index(grid)
        empty_cols = get_empty_columns_index(grid)
        coords = get_coords(grid)
        res = {}
        multiplier = 1_000_000

        count_rows = 0
        count_cols = 0

        for i, (label1, c1) in enumerate(coords):
            cx1 = c1[0] + get_bellow_count(empty_rows, c1[0])*multiplier - get_bellow_count(empty_rows, c1[0])
            cy1 = c1[1] + get_bellow_count(empty_cols, c1[1])*multiplier - get_bellow_count(empty_cols, c1[1])

            for j, (label2, c2) in enumerate(coords):
                cx2 = c2[0] + get_bellow_count(empty_rows, c2[0])*multiplier-get_bellow_count(empty_rows, c2[0])
                cy2 = c2[1] + get_bellow_count(empty_cols, c2[1])*multiplier-get_bellow_count(empty_cols, c2[1])

                if (label1, label2) in res or (label2, label1) in res:
                    continue
                if c1 == c2:
                    continue
                else:
                    m = get_manhattan((cx1, cy1), (cx2, cy2))
                    res[(label1, label2)] = m

        suma = 0
        for key in res:
            suma += res[key]
        print(suma)
