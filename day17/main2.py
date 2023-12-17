from heapq import heapify, heappush, heappop

def print_state(came_from, board, current):
    board_out = [[str(i) for i in row] for row in board]
    node = current
    while node:
        (i, j), direct, _ = node
        
        if node[0] == (0, 0):
            break
        if direct == "R":
            board_out[i][j] = ">"
        if direct == "L":
            board_out[i][j] = "<"
        if direct == "U":
            board_out[i][j] = "^"
        if direct == "D":
            board_out[i][j] = "v"
        node = came_from[node]

    for row in board_out:
        print(row)


def move(board, row, col, direction):
    if direction == "L":
        if col > 0:
            return row, col-1
        return None
    if direction == "R":
        if col < len(board[0])-1:
            return row, col+1
        return None
    if direction == "U":
        if row > 0:
            return row-1, col
        return None
    if direction == "D":
        if row < len(board)-1:
            return row+1, col
        return None
    return None

def get_neighbours(board, row, col, direction,count):
    neigh = []

    if count < 4 and (row, col) != (0, 0):
        moved = move(board, row, col, direction)
        if moved:
            return [(board[moved[0]][moved[1]], (*moved, direction, count+1))]
        return []
    #lefts
    if col > 0:
        if direction == "L" and count < 10:
            neigh+= [(board[row][col-1], (row, col-1, direction, count+1))]
        elif direction == "L" and count >= 10:
            pass
        elif direction == "R":
            pass
        else:
            neigh+= [(board[row][col-1], (row, col-1, "L", 1))]


    #rights
    if col < len(board[0])-1:
        if direction == "R" and count < 10:
            neigh+= [(board[row][col+1], (row, col+1, direction, count+1))]
        elif direction == "R" and count >= 10:
            pass
        elif direction == "L":
            pass
        else:
            neigh+= [(board[row][col+1], (row, col+1, "R", 1))]
    #up
    if row > 0:
        if direction == "U" and count < 10:
            neigh+= [(board[row-1][col], (row-1, col, direction, count+1))]
        elif direction == "U" and count >= 10:
            pass
        elif direction == "D":
            pass
        else:
            neigh+= [(board[row-1][col], (row-1, col, "U", 1))]
    #Down
    if row < len(board)-1:
        if direction == "D" and count < 10:
            neigh+= [(board[row+1][col], (row+1, col, direction, count+1))]
        elif direction == "D" and count >= 10:
            pass
        elif direction == "U":
            pass
        else:
            neigh+= [(board[row+1][col], (row+1, col, "D", 1))]
    return neigh


def solve(board):
    q = [ (0, (0, 0, None, 0)) ]
    heapify(q)
    #came_from = {}
    i = 0
    visited = {}
    row_num = len(board)-1
    col_num = len(board[0])-1

    while len(q) > 0:
        score, info = heappop(q)
        row, col, direct, count = info

        if row == row_num and col == col_num and count >= 4:
            #print_state(came_from, board, ((row, col), direct, count))
            return score
        
        neighbours = get_neighbours(board, row, col, direct, count)
        for s, (r, c, d, coun) in neighbours:
            item = ((r, c), d, coun)
            if item not in visited or visited[item] > score+s:
                heappush(q, (s+score, (r, c, d, coun)))
                #came_from[((r, c), d, coun)] = ((row,col), direct, count)
                visited[item] = score + s
        i+=1

def parse(lines):
    return [[int(i) for i in l.strip()] for l in lines]

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    board = parse(lines)
    res = solve(board)

    print(res)
