from dataclasses import dataclass
from typing import List

from aoc import get_input

data = get_input(13).splitlines()


def check_pair(p1, p2):
    for i1, i2 in zip(p1, p2):
        match i1, i2:
            case int(), int():
                if i1 < i2:
                    return 'in_order'
                elif i1 > i2:
                    return 'out_of_order'
            case list(), list():
                result = check_pair(i1, i2)
                if result in ['in_order', 'out_of_order']:
                    return result
                if len(i1) < len(i2):
                    return 'in_order'
                if len(i1) > len(i2):
                    return 'out_of_order'
            case list(), int():
                result = check_pair(i1, [i2])
                if result in ['in_order', 'out_of_order']:
                    return result
            case int(), list():
                result = check_pair([i1], i2)
                if result in ['in_order', 'out_of_order']:
                    return result
    if len(p1) < len(p2):
        return 'in_order'
    if len(p1) > len(p2):
        return 'out_of_order'
    return 'match'


def lt(p1, p2):
    return check_pair(p1, p2) == "in_order"


@dataclass
class Message:
    data: List

    def __lt__(self, other):
        return check_pair(self.data, other.data) == "in_order"


all_items = []
part1 = 0
index = 1
while data:
    pair1 = eval(data.pop(0))
    pair2 = eval(data.pop(0))
    all_items.append(Message(pair1))
    all_items.append(Message(pair2))
    if len(data) > 0 and data[0] == "":
        data.pop(0)
    if check_pair(pair1, pair2) == "in_order":
        part1 += index
    index += 1
print("Part 1:", part1)

div_1 = Message([[2]])
div_2 = Message([[6]])
all_items.append(div_1)
all_items.append(div_2)

all_items.sort()
print("Part 2:", (all_items.index(div_1)+1)*(all_items.index(div_2)+1))
