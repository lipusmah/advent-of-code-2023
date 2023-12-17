

with open("./day6/data.txt") as f:
    lines = f.readlines()
    times = [int(i.strip()) for i in lines[0].split(":")[1].strip().split(" ") if i != "" ]
    distances = [int(i.strip()) for i in lines[1].split(":")[1].strip().split(" ") if i != "" ]
    data = zip(times, distances)
    counts = 1
    for time, distance in data:
        c = 0
        for i in range(time):
            left = time-i
            score = i * left
            print(f"{i}, {left}, {score}")
            if score > distance:
                c += 1

        counts *= c
    
    print(counts)