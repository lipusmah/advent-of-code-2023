from functools import cache

def get_direction(start, stop):
    if start[1] < stop[1]:
        return "right"
    if start[1] > stop[1]:
        return "left"
    if start[0] < stop[0]:
        return "bot"
    if start[0] > stop[0]:
        return "top"

def no_move(start, stop):
    direction = get_direction(start, stop)
    if direction == "top":
        start = stop
        stop = (start[0]-1, start[1])
    if direction == "bot":
        start = stop
        stop = (start[0]+1, start[1])
    if direction == "left":
        start = stop
        stop = (start[0], start[1]-1)
    if direction == "right":
        start = stop
        stop = (start[0], start[1]+1)
    return start, stop

def move(start, stop, direction):
    if direction == "left":
        start = stop
        stop = (stop[0], stop[1]-1)
        return start, stop
    if direction == "right":
        start = stop
        stop = (stop[0], stop[1]+1)
        return start, stop
    if direction == "top":
        start = stop
        stop = (stop[0]-1, stop[1])
        return start, stop
    if direction == "bot":
        start = stop
        stop = (stop[0]+1, stop[1])
        return start, stop


def get_moves(board, start=(0, -1), stop=(0, 0)):
    direction = get_direction(start, stop)
    c = board[stop[0]][stop[1]]
    if c == "\\":
        if direction == "right":
            start, stop = move(start, stop, "bot")
        if direction == "left":
            start, stop = move(start, stop, "top")
        if direction == "top":
            start, stop = move(start, stop, "left")
        if direction == "bot":
            start, stop = move(start, stop, "right")
        return [(start, stop)]

    elif c == "/":
        if direction == "right":
            start, stop = move(start, stop, "top")
        if direction == "left":
            start, stop = move(start, stop, "bot")
        if direction == "top":
            start, stop = move(start, stop, "right")
        if direction == "bot":
            start, stop = move(start, stop, "left")
        return [(start, stop)]

    elif c == ".":
        start, stop = no_move(start, stop)
        return [(start, stop)]

    elif c == "|":
        if direction == "top" or direction == "bot":
            start, stop = no_move(start, stop)
            return [(start, stop)]
        else:
            stop1 = (stop[0]-1, stop[1])
            stop2 = (stop[0]+1, stop[1])
            return [(stop, stop1), (stop, stop2)]
    
    elif c == "-":
        if direction == "left" or direction == "right":
            start, stop = no_move(start, stop)
            return [(start, stop)]

        else:
            stop1 = (stop[0], stop[1]-1)
            stop2 = (stop[0], stop[1]+1)
            return [(stop, stop1), (stop, stop2)]

    return start, stop


def solve(board):
    q = [((0, -1), (0, 0))]
    visited = set()
    i = 0
    while len(q) > 0:
        start, stop = q[0]
        if (start, stop) in visited:
            q = q[1:]
            continue
        if stop[0] < 0 or stop[0] > len(board)-1:
            q = q[1:]
            continue
        if stop[1] < 0 or stop[1] > len(board[0])-1:
            q = q[1:]
            continue
        if i != 0:
            visited.add((start, stop))
        moves = get_moves(board, start, stop)
        q = q[1:] + moves
        i += 1
    return visited        

def parse(lines):
    return [tuple([i for i in l.strip()]) for l in lines]

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    
    board = parse(lines)
    visited = solve(tuple(board))
    unique = set()
    
    visited = [((110, 13), (13, 109))]
    for start,stop in visited:
        if (stop[0] >= 0 and stop[0] < len(board)) and (stop[1] >= 0 and stop[1] < len(board[0])):
            unique.add(start)
        if (start[0] >= 0 and start[0] < len(board)) and (start[1] >= 0 and start[1] < len(board[0])):
            unique.add(stop)


    print(unique)
    print(len(unique))

