from heapq import heapify, heappush, heappop

def print_state(board, path, current):
    board_out = [[str(i) for i in row] for row in board]
    for c, (i, j) in enumerate(path):
        if (i,j) != (0, 0):
            i0, j0 = path[c-1]
            direct = direction((i0, j0), (i, j))
            if direct == "R":
                board_out[i][j] = ">"
            if direct == "L":
                board_out[i][j] = "<"
            if direct == "U":
                board_out[i][j] = "^"
            if direct == "D":
                board_out[i][j] = "v"
        else:
            board_out[i][j] = "X"
        
    board_out[current[0]][current[1]] = "*"

    for row in board_out:
        print(row)


def get_neighbours(board, node, dir_count):
    neigh = []
    row, col = node
    direction, count = dir_count
    #left

    if col > 0:
        if direction == "L" and count < 3:
            neigh+= [(board[row][col-1], (row, col-1), (direction, count+1))]
        elif direction == "L" and count >= 3:
            pass
        elif direction == "R":
            pass
        else:
            neigh+= [(board[row][col-1], (row, col-1), ("L", 1))]

    #right
    if col < len(board[0])-1:
        if direction == "R" and count < 3:
            neigh+= [(board[row][col+1], (row, col+1), (direction, count+1))]
        elif direction == "R" and count >= 3:
            pass
        elif direction == "L":
            pass
        else:
            neigh+= [(board[row][col+1], (row, col+1), ("R", 1))]
    #up
    if row > 0:
        if direction == "U" and count < 3:
            neigh+= [(board[row-1][col], (row-1, col), (direction, count+1))]
        elif direction == "U" and count >= 3:
            pass
        elif direction == "D":
            pass
        else:
            neigh+= [(board[row-1][col], (row-1, col), ("U", 1))]
    #Down
    if row < len(board)-1:
        if direction == "D" and count < 3:
            neigh+= [(board[row+1][col], (row+1, col), (direction, count+1))]
        elif direction == "D" and count >= 3:
            pass
        elif direction == "U":
            pass
        else:
            neigh+= [(board[row+1][col], (row+1, col), ("D", 1))]
    return neigh

def create_path(came_from, node, skip_first):
    res = []
    if skip_first and node[0] != (0, 0):
        node = came_from[node]
    while node:
        res.append(node[0])
        if node[0] == (0, 0):
            node = False
            continue
        node = came_from[node]
      
    return res[::-1]

def direction(start, stop):
    if start == None:
        return None
    if start[1] < stop[1]:
        return "R"
    if start[1] > stop[1]:
        return "L"
    if start[0] < stop[0]:
        return "D"
    if start[0] > stop[0]:
        return "U"


def solve(board):
    q = [ (0, ([(0, 0)], None, 0)) ]
    heapify(q)
    i = 0
    visited = set()
    while len(q) > 0:
        score, info = heappop(q)
        path, direct, count = info
        row, col = path[-1]
        visited.add(((row, col), direct))

        print(f"{score}, {row}, {col}")
        if row == len(board)-1 and col == len(board[0])-1:
            print_state(board, path,(row, col))
            return score
        
        neighbours = get_neighbours(board, (row, col), (direct, count))
        for s, (r, c), (d, count) in neighbours:
            if ((r, c), d) not in visited:
                heappush(q, (s+score, (path+ [(r, c)], d, count)))
        i+=1
    
    print_state(board, path,(row, col))


def parse(lines):
    return [[int(i) for i in l.strip()] for l in lines]

if __name__ == "__main__":
    with open("test-input.txt") as f:
        lines = f.readlines()

    board = parse(lines)
    res = solve(board)

    print(res)
