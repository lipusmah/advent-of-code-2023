
def solve_line(line, agg):
    first = int(line[0])
    new_line = [int(line[i+1])-int(line[i]) for i in range(0, len(line)-1)]
    agg.append(first)
    
    if all([i == 0 for i in new_line]):
        return agg
    return solve_line(new_line, agg)

def get_score(solved: list):
    res = 0
    for s in solved[::-1]:
        res = s - res
    return res

if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.readlines()
        lines = [l.strip().split(" ") for l in data]
    res = 0
    for l in lines:
        solved = solve_line(l, [])
        score = get_score(solved)
        res += score
        print(f"{score}, {solved}")

    print(res)