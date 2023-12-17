

with open("./day6/data.txt") as f:
    lines = f.readlines()
    time = int(lines[0].split(":")[-1].replace(" ", ""))
    duration = int(lines[1].split(":")[-1].replace(" ", ""))
    start = int(duration/time) - 1
    counts = 0
    wasbigger = False
    for i in range(start, time):
        left = time-i
        score = i * left
        print(f"{i}, {left}, {score}")
        if score > duration:
            counts += 1
            wasbigger = True
        elif wasbigger:
            break
    print(counts)