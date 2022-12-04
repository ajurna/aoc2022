from aoc import get_input
import string
data = get_input(3).splitlines()

score_table = " "+string.ascii_lowercase+string.ascii_uppercase
score = 0
for line in data:
    ans = (set(line[:len(line)//2]) & set(line[len(line)//2:])).pop()
    score += score_table.index(ans)
print(f"Part 1: {score}")

score = 0
while data:
    bag1 = set(data.pop())
    bag2 = set(data.pop())
    bag3 = set(data.pop())
    ans = bag1 & bag2 & bag3
    score += score_table.index(ans.pop())
print(f"Part 2: {score}")
