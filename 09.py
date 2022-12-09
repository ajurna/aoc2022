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
tail_visited = set(tail)
data = get_input(9).splitlines()
# data ="""U 1
# R 2
# D 2
# L 2
# R 2
# U 2
# """.splitlines()

for line in data:
    d, dis = line.split()
    dis = int(dis)
    for _ in range(dis):
        head: Point = directions[d](head)
        if head.distance(tail) > 1:
            if head.x == tail.x and head.y != tail.y:
                tail = down(tail) if head.y < tail.y else up(tail)
            elif head.x != tail.x and head.y == tail.y:
                tail = left(tail) if head.x < tail.x else right(tail)
            else:
                tail = down(tail) if head.y < tail.y else up(tail)
                tail = left(tail) if head.x < tail.x else right(tail)
            tail_visited.add(tail)
print(len(tail_visited))
