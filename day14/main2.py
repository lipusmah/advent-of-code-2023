import cProfile

def get_cols_rows(lines):
    rs = []
    cs = []
    for i in lines:
        line = i.strip()
        rs.append([c for c in line])
    
    for i in range(len(rs[0])):
        cs.append([r[i] for r in rs])
    
    return rs, cs

def rearrange(row, reverse=False):
    current_stop = 0
    if reverse:
        row = row[::-1]

    for i in range(len(row)):
        c = row[i]
        if c == ".":
            continue
        if c == "#":
            current_stop = i + 1 
        else:
            new_position = current_stop
            if i == new_position:
                current_stop = i + 1 
                continue
            if i == 0:
                current_stop = new_position
                continue
            row[new_position] = "O"
            row[i] = "."
            current_stop = new_position+1
               
    if reverse:
        row = row[::-1]
    return row

def rearrange_board(cols, reverse=False):
    return [rearrange(line, reverse) for line in cols]

def pivot(items):
    return list(map(list, zip(*items)))

def solve2(rows, cols):
    count = 1_000_000_000
    left = 1000
    rows = rows[::]
    cols = cols[::]

    cache = {}
    for c in range(count):
        for r in rows:
            print(r)
        print()
        key = hash(tuple((tuple(r) for r in rows)))
        if key in cache:
            left = (count-c) % (c - cache[key])
            print("repeated at: " + str(left))
            break

        cols = rearrange_board(cols)
        rows = pivot(cols)
        rows = rearrange_board(rows)
        cols = pivot(rows)
        cols = rearrange_board(cols, True)
        rows = pivot(cols)
        rows = rearrange_board(rows, True)
        cols = pivot(rows)

        cache[key] = c

    for c in range(left):
        cols = rearrange_board(cols)
        rows = pivot(cols)
        rows = rearrange_board(rows)
        cols = pivot(rows)
        cols = rearrange_board(cols, True)
        rows = pivot(cols)
        rows = rearrange_board(rows, True)
        cols = pivot(rows)

    calc = 0
    for column in cols:
        for i, char in enumerate(column):
            if char == "O":
                calc += len(column)-i

    print(calc)
    return count

if __name__ == "__main__":
    with open("input.txt") as f:
        srows, scols = get_cols_rows(f.readlines())
        #cProfile.run('solve2(srows, scols)')
        res = solve2(srows, scols)
