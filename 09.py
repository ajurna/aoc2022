from dataclasses import dataclass
from typing import NamedTuple

from aoc import get_input


class Point(NamedTuple):
    x: int
    y: int

    def distance(self, other: "Point"):
        # Chebyshev Distance
        return max(abs(self.x - other.x), abs(self.y - other.y))


def up(p: Point) -> Point:
    return Point(p.x, p.y + 1)


def down(p: Point) -> Point:
    return Point(p.x, p.y - 1)


def right(p: Point) -> Point:
    return Point(p.x + 1, p.y)


def left(p: Point) -> Point:
    return Point(p.x - 1, p.y)


directions = {
    "U": up,
    "D": down,
    "L": left,
    "R": right
}


head = Point(0, 0)
tail = Point(0, 0)
tail_visited = set()
tail_visited2 = set()
tail_visited.add(tail)
tail_visited2.add(tail)
data = get_input(9).splitlines()
# data ="""R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20""".splitlines()


@dataclass
class Rope:
    head: Point
    def __post_init__(self):
        self.body = [self.head] * 10

    def move_body(self):
        self.body[0] = self.head
        for i in range(len(self.body) - 1):
            head = self.body[i]
            tail = self.body[i+1]
            if head.distance(tail) > 1:
                if head.x == tail.x and head.y != tail.y:
                    tail = down(tail) if head.y < tail.y else up(tail)
                elif head.x != tail.x and head.y == tail.y:
                    tail = left(tail) if head.x < tail.x else right(tail)
                else:
                    tail = down(tail) if head.y < tail.y else up(tail)
                    tail = left(tail) if head.x < tail.x else right(tail)
                self.body[i+1] = tail
        tail_visited2.add(self.body[-1])


rope = Rope(Point(0, 0))
for line in data:
    direction, distance = line.split()
    distance = int(distance)
    for _ in range(distance):
        head: Point = directions[direction](head)
        if head.distance(tail) > 1:
            if head.x == tail.x and head.y != tail.y:
                tail = down(tail) if head.y < tail.y else up(tail)
            elif head.x != tail.x and head.y == tail.y:
                tail = left(tail) if head.x < tail.x else right(tail)
            else:
                tail = down(tail) if head.y < tail.y else up(tail)
                tail = left(tail) if head.x < tail.x else right(tail)
            tail_visited.add(tail)
        rope.head = directions[direction](rope.head)
        rope.move_body()

print(f"Part 1:", len(tail_visited))
print(f"Part 2:", len(tail_visited2))

