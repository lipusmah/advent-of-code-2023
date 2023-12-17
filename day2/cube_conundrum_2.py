
def parse_single_color(data: str):
    num, color = data.strip().split(" ")
    return num, color


def parse_single_pull(data: str):
    d = {}
    parsed = data.strip().split(",")
    for c in parsed:
        num, color = parse_single_color(c)
        d[color] = int(num)
    return d

def parse_line(line: str):
    game, results = line.split(":")
    _, game_id = game.split(" ")
    games = results.split(";")
    max_vals = {"red": 0, "green": 0, "blue": 0}
    for p in games:
        colors = parse_single_pull(p)
        for c in colors:
            if colors[c] > max_vals[c]:
                max_vals[c] = colors[c]
        
    return game_id, max_vals

max_colors = {"green": 13, "red": 12, "blue": 14}

def product(list: list[int]):
    p = 1
    for l in list:
        p *= l
    return p

with open("./cube_games.txt") as f:
    lines= f.readlines()
    sum = 0
    for l in lines:
        game_id, max_values = parse_line(l)
        prod = product([max_values[key] for key in max_values])
        sum += prod
    print(sum) 