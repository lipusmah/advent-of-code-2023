# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?


def get_first_digit(string, reverse=False):
    if reverse:
        string = string[::-1]
    for c in string:
        if c.isnumeric():
            return c
    return None

with open("./calibration_values.txt") as f:
    lines = f.readlines()
    res = sum([int(get_first_digit(l.strip()) + get_first_digit(l.strip(), True)) for l in lines])
    print(res)
    