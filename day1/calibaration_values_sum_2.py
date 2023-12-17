numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def check_string_number(digit_string):
    for key in numbers:
        if key in digit_string:
            return numbers[key]
    
    return None

def get_first_digit(string, reverse=False) -> str:
    if reverse:
        string = string[::-1]
    passed = ""
    for c in string:
        if c.isnumeric():
            return c
        if reverse:
            passed = c + passed
        else:
            passed += c
        
        stringnum = check_string_number(passed)
        if stringnum is not None:
            return str(stringnum)

    return None

with open("./calibration_values.txt") as f:
    lines = f.readlines()
    res = sum([int(get_first_digit(l.strip()) + get_first_digit(l.strip(), True)) for l in lines])
    print(res)
    