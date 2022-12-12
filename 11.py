from dataclasses import dataclass
from typing import List, Callable

from aoc import get_input

data = get_input(11).splitlines()


@dataclass
class Monkey:
    items: List[int]
    operation: Callable
    test: int
    true_monkey: int
    false_monkey: int
    inspected: int = 0

    def __lt__(self, other):
        return self.inspected < other.inspected

monkeys = [
    Monkey(items=[57, 58], operation=lambda x: x * 19, test=7, true_monkey=2, false_monkey=3),
    Monkey(items=[66, 52, 59, 79, 94, 73], operation=lambda x: x + 1, test=19, true_monkey=4, false_monkey=6),
    Monkey(items=[80], operation=lambda x: x + 6, test=5, true_monkey=7, false_monkey=5),
    Monkey(items=[82, 81, 68, 66, 71, 83, 75, 97], operation=lambda x: x + 5, test=11, true_monkey=5, false_monkey=2),
    Monkey(items=[55, 52, 67, 70, 69, 94, 90], operation=lambda x: x * x, test=17, true_monkey=0, false_monkey=3),
    Monkey(items=[69, 85, 89, 91], operation=lambda x: x + 7, test=13, true_monkey=1, false_monkey=7),
    Monkey(items=[75, 53, 73, 52, 75], operation=lambda x: x * 7, test=2, true_monkey=0, false_monkey=4),
    Monkey(items=[94, 60, 79], operation=lambda x: x + 2, test=3, true_monkey=1, false_monkey=6)
]

for _ in range(20):
    for monkey in monkeys:
        while monkey.items:
            worry = monkey.operation(monkey.items.pop()) // 3
            monkey.inspected += 1
            if worry % monkey.test:
                monkeys[monkey.false_monkey].items.append(worry)
            else:
                monkeys[monkey.true_monkey].items.append(worry)
m1, m2 = sorted(monkeys, reverse=True)[:2]
print("Part 1:", m1.inspected * m2.inspected)

monkeys = [
    Monkey(items=[57, 58], operation=lambda x: x * 19, test=7, true_monkey=2, false_monkey=3),
    Monkey(items=[66, 52, 59, 79, 94, 73], operation=lambda x: x + 1, test=19, true_monkey=4, false_monkey=6),
    Monkey(items=[80], operation=lambda x: x + 6, test=5, true_monkey=7, false_monkey=5),
    Monkey(items=[82, 81, 68, 66, 71, 83, 75, 97], operation=lambda x: x + 5, test=11, true_monkey=5, false_monkey=2),
    Monkey(items=[55, 52, 67, 70, 69, 94, 90], operation=lambda x: x * x, test=17, true_monkey=0, false_monkey=3),
    Monkey(items=[69, 85, 89, 91], operation=lambda x: x + 7, test=13, true_monkey=1, false_monkey=7),
    Monkey(items=[75, 53, 73, 52, 75], operation=lambda x: x * 7, test=2, true_monkey=0, false_monkey=4),
    Monkey(items=[94, 60, 79], operation=lambda x: x + 2, test=3, true_monkey=1, false_monkey=6)
]

lcm = 9699690
for _ in range(10000):
    for monkey in monkeys:
        while monkey.items:
            worry = monkey.operation(monkey.items.pop())
            if worry > lcm:
                worry = worry % lcm
            monkey.inspected += 1
            if worry % monkey.test:
                monkeys[monkey.false_monkey].items.append(worry)
            else:
                monkeys[monkey.true_monkey].items.append(worry)
m1, m2 = sorted(monkeys, reverse=True)[:2]
print("Part 2:", m1.inspected * m2.inspected)