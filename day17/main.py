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


def get_neighbours(board, row, col, direction,count):
    neigh = []

    if col > 0:
        if direction == "L" and count < 3:
            neigh+= [(board[row][col-1], (row, col-1, direction, count+1))]
        elif direction == "L" and count >= 3:
            pass
        elif direction == "R":
            pass
        else:
            neigh+= [(board[row][col-1], (row, col-1, "L", 1))]

    #right
    if col < len(board[0])-1:
        if direction == "R" and count < 3:
            neigh+= [(board[row][col+1], (row, col+1, direction, count+1))]
        elif direction == "R" and count >= 3:
            pass
        elif direction == "L":
            pass
        else:
            neigh+= [(board[row][col+1], (row, col+1, "R", 1))]
    #up
    if row > 0:
        if direction == "U" and count < 3:
            neigh+= [(board[row-1][col], (row-1, col, direction, count+1))]
        elif direction == "U" and count >= 3:
            pass
        elif direction == "D":
            pass
        else:
            neigh+= [(board[row-1][col], (row-1, col, "U", 1))]
    #Down
    if row < len(board)-1:
        if direction == "D" and count < 3:
            neigh+= [(board[row+1][col], (row+1, col, direction, count+1))]
        elif direction == "D" and count >= 3:
            pass
        elif direction == "U":
            pass
        else:
            neigh+= [(board[row+1][col], (row+1, col, "D", 1))]
    return neigh


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
    q = [ (0, (0, 0, None, 0)) ]
    heapify(q)
    came_from = {}
    i = 0
    visited = {}
    row_num = len(board)-1
    col_num = len(board[0])-1

    while len(q) > 0:
        score, info = heappop(q)
        row, col, direct, count = info

        if row == row_num and col == col_num:
            print(i)
            #print_state(came_from, board, ((row, col), direct, count))
            return score
        
        print(score)
        #print_state(came_from, board, ((row, col), direct, count))
        
        # visited[((row, col), direct, count)] = score
        neighbours = get_neighbours(board, row, col, direct, count)
        
        print()
        
        for s, (r, c, d, coun) in neighbours:
            item = ((r, c), d, coun)
            if item not in visited or visited[item] > score+s:
                heappush(q, (s+score, (r, c, d, coun)))
                came_from[((r, c), d, coun)] = ((row,col), direct, count)
                visited[item] = score + s
            else:
                print(f"skipped: {item}")
        i+=1

def parse(lines):
    return [[int(i) for i in l.strip()] for l in lines]

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    board = parse(lines)
    # cProfile.run("solve(boarçd)")
    res = solve(board)

    print(res)
