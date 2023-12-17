def get_cols_rows(lines):
    cols =[]
    boards =[]

    rs = []
    cs = []
    for i in lines:
        line = i.strip()
        if line == "":
            boards.append(rs)
            rs = []
            continue
        rs.append(line)
    boards.append(rs)
    for b in boards:
        for i in range(len(b[0])):
            res = "".join([r[i] for r in b])
            cs.append(res)
        
        cols.append(cs)
        cs = []
    
    return boards, cols

def get_str_diff(str1, str2):
    diff = []
  
    for i, c1 in enumerate(str1):
        c2 = str2[i]
        if c1 != c2:
            diff.append(c1)
  
    return diff

def check_same(list, i1, i2):
    if i1 == -1:
        # print(f"{list[i1+1]}      {list[i2-1]}, same")
        return True
    if i2 == len(list):
        # print(f"{list[i1+1]}      {list[i2-1]}, same")
        return True

    if list[i1] == list[i2]:
        return check_same(list, i1-1, i2+1)
    
    return False

def check_same_fixed(list, i1, i2):
    if i1 == -1:
        return False
    if i2 == len(list):
        return False
    
    diff = get_str_diff(list[i1], list[i2])
    if list[i1] == list[i2]:
        return check_same_fixed(list, i1-1, i2+1)
    elif len(diff) == 1:
        return check_same(list, i1-1, i2+1)
    
    return False

def get_mirror_index(list):
    for i in range(len(list)-1):
        r1 = list[i]
        r2 = list[i+1]
        if r1 == r2:
            if check_same(list, i, i+1):
                return i+1
    
    return None

def get_fixed_mirror_index(list):
    
    for i in range(len(list)-1):
        r1 = list[i]
        r2 = list[i+1]
        diff = get_str_diff(r1, r2)
        
        if len(diff) <= 1:
            if check_same_fixed(list, i, i+1):
                return i + 1
    
    return None

def solve(lines:list[str]):
    boards, columns = get_cols_rows(lines)
    suma = 0
    for i, board in enumerate(boards):
        cols = columns[i]
    
        x = get_fixed_mirror_index(board)
        y = get_fixed_mirror_index(cols)
        
        print(f"{x}, {y}")
        if x is not None:
            suma += x*100

        if y is not None:
            suma += y
    print(suma)

if __name__ == "__main__":
    with open("input.txt") as f:
        res = solve(f.readlines())
        print(res)
