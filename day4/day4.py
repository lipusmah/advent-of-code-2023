def parse_line(line: str):
    left, right = line.strip().split("|")
    _, nums = left.strip().split(":")
    nums = nums.strip().replace("  ", " ")
    right = right.strip().replace("  ", " ")

    my_nums = [int(n) for n in right.strip().split(" ")]
    nums = [int(n) for n in nums.strip().split(" ")]
    return set(nums), my_nums


with open("./day4/data.txt") as f:
    total = 0
    for l in f.readlines():
        s = 0
        line = l.strip()
        nums, my_nums = parse_line(line)
        for n in my_nums:
            if n in nums:
                if s == 0:
                    s = 1
                else:
                    s = s*2
        total += s
    print(total)