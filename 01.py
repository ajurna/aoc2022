from dataclasses import dataclass

from aoc import get_input

data = get_input(1).splitlines()


@dataclass
class Elf:
    calories: int = 0

    def __lt__(self, other):
        return self.calories < other.calories


current_elf = Elf()
elves = [current_elf]
for line in data:
    match line:
        case "":
            current_elf = Elf()
            elves.append(current_elf)
        case _:
            current_elf.calories += int(line)
elves.sort(reverse=True)
print(f"Part 1: {elves[0].calories}")
print(f"Part 2: {sum(elf.calories for elf in elves[0:3])}")
