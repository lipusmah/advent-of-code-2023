def parse_first_line(line: str):
    _, seeds = line.split(":")
    seeds = seeds.strip().split(" ")
    return [int(s) for s in seeds]

def parse_lines(lines: list[str]):
    map_inputs = {}
    c = 0
    last_header = None
    for l in lines:
        line = l.strip()
        if len(line) == 0:
            continue
        if not line[0].isnumeric():
            h = line.split(" ")[0]
            head = h.split("-")
            last_header = (head[0], head[-1])
            map_inputs[last_header] = []
        elif line[0].isnumeric():
            map_inputs[last_header].append([int(c) for c in line.split(" ")])
        
    return map_inputs

with open("./day5/data.txt") as f:
    lines = f.readlines()
    
    seeds = parse_first_line(lines[0])
    maps = parse_lines(lines[1:])
    
    minimum = float('inf')
    
    for s in seeds:
        current = s
        for mapkey in maps:
            m = maps[mapkey]
            for dest, source, rang in m:
                if source < current < source+rang:
                    print(f"map: {mapkey}, {current}, diff: {dest-source}, dest: {current + (dest-source)}")
                    current = current + (dest-source)
                    break
        if current < minimum:
            minimum = current
        print("")

    print(f"res: {minimum}")
