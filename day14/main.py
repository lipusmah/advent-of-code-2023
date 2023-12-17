def get_cols_rows(lines):
    rs = []
    cs = []
    for i in lines:
        line = i.strip()
        rs.append(line)
    
    for i in range(len(rs[0])):
        res = "".join([r[i] for r in rs])
        cs.append(res)
    
    return rs, cs

def rearrange(row):
    stone_c = 0
    ind_count = 0
    stone_moves = []
    for i, c in enumerate(row):
        if c == ".":
            continue
        if c == "#":
            ind_count = i + 1 
        else:
            new_position = ind_count
            if i == new_position:
                ind_count = i + 1 
                continue
            if i == 0:
                ind_count = new_position
                continue
            stone_moves.append((i, new_position))
            ind_count = new_position+1
           
    new_row = row[::]
    
    for move_start, move_end in stone_moves:
        new_row = new_row[:move_end] + "O" + new_row[move_end+1:]
        new_row = new_row[:move_start] + "." + new_row[move_start+1:]
    
    return new_row


def solve(cols):
    rearranged = []
    calc = 0
    for l in cols:
        line = l.strip()
        arranged = rearrange(line)
        for i, c in enumerate(arranged):
            if c == "O":
                calc += len(arranged)-i
        print(arranged)
        rearranged.append(arranged)
    print(calc)
    return calc

if __name__ == "__main__":
    with open("test-input.txt") as f:
        rows, cols = get_cols_rows(f.readlines())
        res = solve(cols)
        print(res)
