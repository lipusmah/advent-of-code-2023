def get_graph(lines: list[str]):
    graph = {}
    start = None
    for i, line in enumerate(lines):
        for j, char in enumerate(line.strip()):
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

    i, j= start

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

    return graph, start


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
    queue = [start]
    c = 1
    visited_set = set()
    while len(queue) > 0:
        current = queue.pop()
        if start in graph[current] and c > 2:
            return c
        for neighbour in graph[current]:
            if neighbour not in visited_set:
                queue.append(neighbour)

        visited_set.add(current)
        c += 1

    return c

if __name__ == "__main__":
    with open("input.txt") as f:
        graph, start = get_graph(f.readlines())
        assert (start[0], start[1]) in graph
        res = get_start_loop_length(graph, start)

        print(res, int(res/2))

    
    
