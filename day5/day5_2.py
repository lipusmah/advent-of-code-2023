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

def get_intersection(lowx, lowy, highx, highy):
    mini = max(lowx, lowy)
    maxi = min(highx, highy)
    return [mini, maxi]

def get_difference(lowx, lowy, highx, highy) -> list[list]:
    if lowx > lowy and highy < highx:
        return [[highy, highx]]
    elif lowx < lowy and highx < highy:
        return [[lowx, lowy]]
    elif lowx < lowy and highx > highy:
        return [[lowx, lowy], [highy, highx]]
    elif lowx > lowy and highx > highy:
        return [[lowy, lowx], [highy, highx]]
    return None

with open("./day5/test-data.txt") as f:
    lines = f.readlines()
    
    seeds = parse_first_line(lines[0])
    maps = parse_lines(lines[1:])
    
    minimum = float('inf')
    seed_ranges = zip(*[iter(seeds)]*2)
    ranges = [[seed, seed+r] for seed, r in seed_ranges]

    for seed_start, seed_stop in ranges:
        aggregate = [[seed_start, seed_stop]]
        
        for mapkey in maps:
            new = []
            m = maps[mapkey]

            for start, stop in aggregate:
                created = False            
                for dest, source, rang in m:
                    source_stop = source+rang-1
                    inter = get_intersection(source, start, source_stop, stop)
                    if inter[0] < inter[1]:
                        shift = dest-source
                        new.append([start + shift, min(source_stop, stop) + shift])
                        if source_stop < stop:
                            start = source_stop-1
                        created = True
                
                    if not created:
                        new.append([start, stop])
                
            aggregate = new

        mini = min([i[0] for i in aggregate])
        if mini < minimum:
            minimum = mini
                
       
    print(f"res: {minimum}")
