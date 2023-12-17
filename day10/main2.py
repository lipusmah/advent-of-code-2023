from shapely.geometry import Polygon

def get_graph(lines: list[str]):
    graph = {}
    start = None
    maxi = 0
    maxj = 0

    for i, line in enumerate(lines):
        mini = i
        for j, char in enumerate(line.strip()):
            maxj = j
            if char == "|":
                graph[(i, j)] = [(i - 1, j), (i + 1, j)]
            if char == "-":
                graph[(i, j)] = [(i, j - 1), (i, j + 1)]
            if char == "L":
                graph[(i, j)] = [(i - 1, j), (i, j + 1)]
            if char == "J":
                graph[(i, j)] = [(i - 1, j), (i, j - 1)]
            if char == "7":
                graph[(i, j)] = [(i, j - 1), (i + 1, j)]
            if char == "F":
                graph[(i, j)] = [(i, j + 1), (i + 1, j)]
            if char == "S":
                start = (i, j)

    i, j = start

    adjacent = check_adjacent(graph, i, j)

    if "left" in adjacent and "right" in adjacent:
        graph[(i, j)] = [(i, j - 1), (i, j + 1)]

    if "left" in adjacent and "top" in adjacent:
        graph[(i, j)] = [(i - 1, j), (i, j - 1)]

    if "left" in adjacent and "bot" in adjacent:
        graph[(i, j)] = [(i, j - 1), (i + 1, j)]

    if "top" in adjacent and "bot" in adjacent:
        graph[(i, j)] = [(i - 1, j), (i + 1, j)]
    if "top" in adjacent and "left" in adjacent:
        graph[(i, j)] = [(i - 1, j), (i, j - 1)]
    if "top" in adjacent and "right" in adjacent:
        graph[(i, j)] = [(i - 1, j), (i, j + 1)]

    if "right" in adjacent and "bot" in adjacent:
        graph[(i, j)] = [(i, j + 1), (i + 1, j)]
    if "right" in adjacent and "left" in adjacent:
        graph[(i, j)] = [(i, j - 1), (i, j + 1)]
    if "right" in adjacent and "top" in adjacent:
        graph[(i, j)] = [(i - 1, j), (i, j - 1)]

    if "bot" in adjacent and "top" in adjacent:
        graph[(i, j)] = [(i - 1, j), (i + 1, j)]
    if "bot" in adjacent and "left" in adjacent:
        graph[(i, j)] = [(i, j - 1), (i + 1, j)]
    if "bot" in adjacent and "right" in adjacent:
        graph[(i, j)] = [(i, j + 1), (i + 1, j)]

    return graph, start, maxi, maxj


def check_adjacent(graph, i, j):
    res = []
    if (i - 1, j) in graph and (i, j) in graph[(i - 1, j)]:
        res.append("top")
    if (i + 1, j) in graph and (i, j) in graph[(i + 1, j)]:
        res.append("bot")
    if (i, j - 1) in graph and (i, j) in graph[(i, j - 1)]:
        res.append("left")
    if (i, j + 1) in graph and (i, j) in graph[(i, j + 1)]:
        res.append("right")
    return res


def get_start_loop_length(graph, start):
    parents = {start: None}
    queue = [start]
    c = 1
    visited_set = set()
    while len(queue) > 0:
        current = queue.pop()
        if start in graph[current] and c > 2:
            cur = current
            path = [start]
            while cur:
                path.append(cur)
                if cur == start:
                    return path[::-1]
                cur = parents[cur]

        for neighbour in graph[current]:
            if neighbour not in visited_set:
                queue.append(neighbour)
                parents[neighbour] = current

        visited_set.add(current)
        c += 1
    return None


def get_path(graph, start, stop):
    parents = {start: None}
    queue = [start]
    c = 1
    visited_set = set()
    while len(queue) > 0:
        current = queue.pop()
        if current[0] < 0 or current[1] < 0:
            continue

        if stop in graph[current] and c > 2:
            cur = current
            path = [stop]
            
            while cur:
                path.append(cur)
                if cur == start:
                    return path[::-1]
                cur = parents[cur]

        for neighbour in graph[current]:
            if neighbour not in visited_set:
                queue.append(neighbour)
                parents[neighbour] = current

        visited_set.add(current)
        c += 1
    print(c)
    return None


def get_second_graph(lines, path):
    graph = {}
    for i, line in enumerate(lines):
        line = line.strip()
        for j, char in enumerate(line.strip()):
            if (i, j) in path:
                continue

            left = [l for l in path if l[0] == i and l[1] < j and line[l[1]] != "-" ]
            right = [l for l in path if l[0] == i and l[1] > j and line[l[1]] != "-" ]
            top = [l for l in path if l[1] == j and l[0] < i and line[l[0]] != "|" ]
            bot = [l for l in path if l[1] == j and l[0] > i and line[l[0]] != "|" ]

            # if len(left) == 0 or len(right) == 0 or len(top) == 0 or len(bot) == 0:
            #     return False
            print()

            # if (i + 1, j) not in path and i < len(lines)-1:
            #     graph[(i, j)].append((i + 1, j))
            # if (i - 1, j) not in path and i > 0:
            #     graph[(i, j)].append((i - 1, j))
            # if (i, j + 1) not in path and j < len(line.strip())-1:
            #     graph[(i, j)].append((i, j + 1))
            # if (i, j - 1) not in path and j > 0:
            #     graph[(i, j)].append((i, j - 1))



    return graph


if __name__ == "__main__":
    with open("test-input.txt") as f:
        lines = f.readlines()
        graph, start, maxi, maxj = get_graph(lines)

        assert (start[0], start[1]) in graph
        path = get_path(graph, start, start)
        p = Polygon(path)
        print(p.area)
        second_graph = get_second_graph(lines, path)
        count = 0
        print(count)
