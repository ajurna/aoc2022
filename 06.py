from aoc import get_input
from collections import Counter

data = get_input(6).strip()

for i in range(len(data)):
    if len(Counter(data[i:i+4])) == 4:
        print("Part 1:", i+4)
        break

for i in range(len(data)):
    if len(Counter(data[i:i+14])) == 14:
        print("Part 2:", i + 14)
        break