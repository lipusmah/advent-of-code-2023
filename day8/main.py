import re
from itertools import cycle
from math import lcm

graph: dict[str, tuple[str, str]] = {}
turns: str = None

with open("./day8/data.txt") as f:
    lines = f.readlines()
    
pattern = re.compile(r'\b[A-Z0-9]{3}\b')

start = "AAA"
stop = "ZZZ"


for i, l in enumerate(lines):
    if l.strip() == "":
        continue
    if i == 0:
        turns = l.strip()
    else:
        matches = pattern.findall(l.strip())
        graph[matches[0]] = (matches[1], matches[2])

i = 0
c = 0

currents = [k for k in graph if k[-1] == "A"]

print("running...")
first_visited = set([currents[0]])
results = []

for c in currents:
    key = c
    for i, turn in enumerate(cycle(turns), 1):
        key = graph[key][turn == "R"]
        if key.endswith("Z"):
            results.append(i)
            break
res = lcm(*results)
print (res)


print(f"{c}, {currents}")