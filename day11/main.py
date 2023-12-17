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

def duplicate_empty_rows(grid):
    updated = []
    for row in grid:
        if all([r == 0 for r in row]):
            updated.append(row)
            updated.append(copy.deepcopy(row))
        else:
            updated.append(row)
    return updated

def duplicate_empty_columns(grid):
    k = 0
    result = copy.deepcopy(grid)
    for i in range(len(grid[0])):
        col = [row[i] for row in grid]
        print(i)
        
        if all([row[i] == 0 for row in grid]):
            for j in range(len(grid)):
                result[j].insert(i+k, 0)
            k += 1
    return result

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


if __name__ == "__main__":
    with open("input.txt") as f:
        grid = get_grid(f.readlines())
        updated = duplicate_empty_rows(grid)
        updated2 = duplicate_empty_columns(updated)
        coords = get_coords(updated2)
        res = {}
        for label1, coord in coords:
            for j, (label2, c2) in enumerate(coords):
                if (label1, label2) in res or (label2, label1) in res:
                    continue
                if coord == c2:
                    continue
                else:
                    m = get_manhattan(coord, c2)
                    res[(label1, label2)] = m
        suma = 0
        for key in res:
            suma += res[key]
        print(res)
        print(suma)
