
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
    isValid = True
    for p in games:
        colors = parse_single_pull(p)
        for c in colors:
            if colors[c] > max_colors[c]:
                isValid = False
    return game_id, isValid

max_colors = {"green": 13, "red": 12, "blue": 14}

with open("./cube_games.txt") as f:
    lines= f.readlines()
    sum = 0
    for l in lines:
        game_id, valid = parse_line(l)
        if valid:
            sum += int(game_id)
    print(sum)