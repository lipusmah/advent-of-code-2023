import copy
from itertools import cycle


def get_single_solution():
    return

def get_grouped_codes(codes):
    grouped_codes = {}
    current_codes = []
    current = codes[0]
    count = 0
    for c in codes:
        if c != current:
            grouped_codes[count] = copy.deepcopy(current_codes)
            current_codes = [c]
            count += 1
        else:
            current = c
            current_codes.append(c)
    return grouped_codes

def solve_line(codes, groups):
    count = 0
    options = []
    val = 0

    prev = None

    gs = copy.deepcopy(groups)
    breaked = False
    for i, c in enumerate(codes):
        group = gs[0]
        try:
            nex = codes[i+1]
        except:
            nex = None

        if c == "?":
            options = []
            option1 = codes[:i] + "#" + codes[i+1:]
            option2 = codes[:i] + "." + codes[i+1:]

            if prev == "#" and breaked:
                return solve_line(option2, copy.deepcopy(groups))
   
            if prev == "#" and count < group:
                return solve_line(option1, copy.deepcopy(groups))            

            return solve_line(option1, copy.deepcopy(groups)) + solve_line(option2, copy.deepcopy(groups))
        
        if c == "#":
            count += 1
        if c == "." and count < group and count > 0:
            return 0
        if count == group and nex != "#":
            gs=gs[1:]
            count = 0
            breaked = True
            if len(gs) == 0 and "#" not in codes[i+1:]:                    
                return 1
            elif len(gs) == 0:
                return 0
        elif count == group and nex == "#":
            return 0
        else:
            breaked = False
        prev = c
    if len(gs) == 0 and count == 0:                    
        return 1
    return 0

def solve(lines:list[str]):
    sums = {}
    suma = 0
    for i, l in enumerate(lines):
        line = l.strip()
        print(line)
        codes, groups = line.split(" ")
        groups = [int(g) for g in groups.split(",")]
        codes = "?".join([codes for i in range(5)])
        permutation = solve_line(codes, groups*5)
        print(f"{codes}, {groups*5}, {permutation}")
        suma += permutation
    return suma

if __name__ == "__main__":
    with open("test-input.txt") as f:
        res = solve(f.readlines())
        print(res)
