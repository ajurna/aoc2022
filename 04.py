from aoc import get_input

data = get_input(4).splitlines()

score = 0
score2 = 0
for line in data:
    section1, section2 = line.split(',')
    s1_start, s1_end = section1.split('-')
    s2_start, s2_end = section2.split('-')
    section1 = set(range(int(s1_start), int(s1_end) + 1))
    section2 = set(range(int(s2_start), int(s2_end) + 1))
    if section1.issubset(section2) or section2.issubset(section1):
        score += 1
    if section1.intersection(section2):
        score2 += 1

print(f"Part 1: {score}")
print(f"Part 2: {score2}")
