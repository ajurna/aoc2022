from aoc import get_input

data = get_input(2).splitlines()

score = 0
for line in data:
    game = line.split()
    match game:
        case["A", "X"]:
            score += 1 + 3
        case["A", "Y"]:
            score += 2 + 6
        case["A", "Z"]:
            score += 3
        case["B", "X"]:
            score += 1
        case["B", "Y"]:
            score += 2 + 3
        case["B", "Z"]:
            score += 3 + 6
        case["C", "X"]:
            score += 1 + 6
        case["C", "Y"]:
            score += 2
        case["C", "Z"]:
            score += 3 + 3
print(f"Part 1: {score}")

score = 0
for line in data:
    game = line.split()
    match game:
        case["A", "X"]:
            score += 3 + 0
        case["A", "Y"]:
            score += 1 + 3
        case["A", "Z"]:
            score += 2 + 6
        case["B", "X"]:
            score += 1
        case["B", "Y"]:
            score += 2 + 3
        case["B", "Z"]:
            score += 3 + 6
        case["C", "X"]:
            score += 2
        case["C", "Y"]:
            score += 3 + 3
        case["C", "Z"]:
            score += 1 + 6
print(f"Part 2: {score}")
