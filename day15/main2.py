def parse(line):
    return [i.strip() for i in line[0].strip().split(",")]

def calculate_step(step: str, val=0):
    for c in step:
        v = val + ord(c)
        v *= 17
        val = v%256

    return val

if __name__ == "__main__":
    with open("test-input.txt") as f:
        steps = parse(f.readlines())
        result = 0
        for step in steps:
            val = calculate_step(step)
            result += val
            print(val)
    
        print(f"result: {result}")
