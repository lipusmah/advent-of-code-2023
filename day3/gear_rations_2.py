def get_number_item(i, passed_chars):
    str_range = []
    for j, _ in enumerate(passed_chars):
        str_range.append(i - j)
    return (int(passed_chars), str_range)


def parse_line(line: str) -> list[dict[int, int], list[int]]:
    passed = ""
    numbers = []
    stars = []
    for i, c in enumerate(line):
        if c.isnumeric():
            passed += c
            continue
        elif c == ".":
            if passed != "":
                n = get_number_item(i, passed)
                numbers.append(n)
            passed = ""
        elif c == "*":
            if passed != "":
                n = get_number_item(i, passed)
                numbers.append(n)
            passed = ""
            stars.append(i + 1)

    if passed != "":
        n = get_number_item(i, passed)
        numbers.append(n)
    return numbers, stars


def get_adjacent_numbers(line_index, star_index, number_lines):
    if line_index != 0:
        preline = number_lines[line_index - 1]
    else:
        preline = None

    try:
        line = number_lines[line_index]
    except:
        line = None

    if line_index < len(number_lines) - 1:
        postline = number_lines[line_index + 1]
    else:
        postline = None

    adj = []
    if line is not None:
        for num, inds in line:
            if star_index in inds or star_index - 1 in inds or star_index + 1 in inds:
                adj.append(num)

    if preline is not None:
        for num, inds in preline:
            if star_index in inds or star_index - 1 in inds or star_index + 1 in inds:
                adj.append(num)

    if postline is not None:
        for num, inds in postline:
            if star_index in inds or star_index - 1 in inds or star_index + 1 in inds:
                adj.append(num)

    return adj


def get_gear_num(line_index, star_line, number_lines):
    nums = []
    for star in star_line:
        adj = get_adjacent_numbers(line_index, star, number_lines)
        if len(adj) == 2:
            nums.append(adj[0] * adj[1])
    return nums


with open("./data.txt") as f:
    number_lines = []
    symbol_lines = []
    sum_lines = 0

    for i, line in enumerate(f.readlines()):
        numbers_map, symbols = parse_line(line.strip())
        number_lines.append(numbers_map)
        symbol_lines.append(symbols)

    for j, star_line in enumerate(symbol_lines):
        if len(star_line) > 0:
            gear_nums = get_gear_num(j, star_line, number_lines)
            sum_lines += sum(gear_nums)
    print(sum_lines)
