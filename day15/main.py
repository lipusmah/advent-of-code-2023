def parse(line):
    return [i.strip() for i in line[0].strip().split(",")]

def get_hash(step: str, val=0):
    for c in step:
        v = val + ord(c)
        v *= 17
        val = v % 256
    return val

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    steps = parse(lines)
    boxes = [{} for _ in range(256)]

    for i, step in enumerate(steps):
        if step[-1].isnumeric():
            # step has "=" sign
            label, focal_length = step.split("=")
            hash_key = get_hash(label)
            boxes[hash_key][label] = int(focal_length)
        else:
            # step has "-" sign
            label = step[:-1]
            hash_key = get_hash(label)
            if label in boxes[hash_key]:
                del boxes[hash_key][label]

    result = 0
    for hash_key, box in enumerate(boxes):
        multiplier = 1 + hash_key
        for i, lens in enumerate(box):
            val = multiplier * (i + 1)
            val *= box[lens]            
            result += val 

    print(f"result: {result}")
