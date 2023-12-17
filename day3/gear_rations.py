
def get_number_item(i, passed_chars):
    str_range = []
    for j, _ in enumerate(passed_chars):
        str_range.append(i-j)
    return (int(passed_chars), str_range)
    

def parse_line(line: str) -> list[dict[int, int], list[int]]: 
      passed = ""
      numbers = []
      symbols = []
      for i, c in enumerate(line):
            if c.isnumeric():
                passed += c
                continue
            elif c == ".":
                if passed != "":
                    n = get_number_item(i, passed)
                    numbers.append(n)
                passed = ""
            else:
                if passed != "":
                    n = get_number_item(i, passed)
                    numbers.append(n)   
                passed = ""
                symbols.append(i+1)
      if passed != "":
            n = get_number_item(i, passed)
            numbers.append(n)
      return numbers, symbols


def has_adjacent_symbol(line_index, number_item, symbol_lines):
    if line_index != 0:
        preline = symbol_lines[line_index-1]
    else:
        preline = None
    
    try:
        line = symbol_lines[line_index]
    except:
        line = None
    
    if line_index < len(symbol_lines)-1:
        postline = symbol_lines[line_index+1]
    else:
        postline = None
    
    indicies = number_item[1]

    if line is not None:
        for ind in indicies:
            if ind in line or ind-1 in line or ind+1 in line:
                return True

    if preline is not None:
        for ind in indicies:
            if ind in preline or ind-1 in preline or ind+1 in preline:
                return True
            
    if postline is not None:
        for ind in indicies:
            if ind in postline or ind-1 in postline or ind+1 in postline:
                return True
            
    return False


def delete_row_numbers(line_index, number_line, symbol_lines):
    numbers = []
    for number in number_line:
        if has_adjacent_symbol(line_index, number, symbol_lines):
            numbers.append(number)
            
    return numbers

with open("./data.txt") as f:
    number_lines = []
    symbol_lines = []
    sum_lines = 0

    for i, line in enumerate(f.readlines()):
        numbers_map, symbols = parse_line(line.strip())
        number_lines.append(numbers_map)
        symbol_lines.append(symbols)

    for j, number_line in enumerate(number_lines):
        numbers = delete_row_numbers(j,number_line, symbol_lines)
        ns = [n[0] for n in numbers]
        s = sum(ns)
        sum_lines += s
        print(s)
    print(sum_lines)        