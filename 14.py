from collections import deque
from typing import NamedTuple, Set

from aoc import get_input

data = get_input(14).splitlines()
# data = """498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines()


class Point(NamedTuple):
    x: int
    y: int

    def down(self):
        return Point(self.x, self.y + 1)

    def down_right(self):
        return Point(self.x + 1, self.y + 1)

    def down_left(self):
        return Point(self.x - 1, self.y + 1)

    def options(self):
        return [Point(self.x, self.y + 1), Point(self.x + 1, self.y + 1), Point(self.x - 1, self.y + 1)]


walls: Set[Point] = set()
sand: Set[Point] = set()
for line in data:
    points = line.split(' -> ')
    for start, end in zip(points, points[1:]):
        x_start, y_start = map(int, start.split(','))
        x_end, y_end = map(int, end.split(','))
        for y in range(min(y_start, y_end), max(y_start, y_end)+1):
            for x in range(min(x_start, x_end), max(x_start, x_end)+1):
                walls.add(Point(x, y))
bottom_height = max(w.y for w in walls)
max_right = max(w.x for w in walls)
min_right = min(w.x for w in walls)
sand_origin = Point(500, 0)
dropping_sand = True
while dropping_sand:
    grain = sand_origin
    dropping = True
    occupied = walls | sand
    while dropping:
        step_down = grain.down()
        step_dl = grain.down_left()
        step_dr = grain.down_right()
        if grain.y > bottom_height:
            dropping_sand = False
            dropping = False
        elif step_down not in occupied:
            grain = step_down
        elif step_dl not in occupied:
            grain = step_dl
        elif step_dr not in occupied:
            grain = step_dr
        else:
            sand.add(grain)
            dropping = False
print("Part 1:", len(sand))


def bfs(start: Point, walls: Set[Point], limit: int):
    visited = set()
    queue = deque()
    queue.append(start)
    while queue:
        node: Point = queue.pop()
        visited.add(node)
        for opt in node.options():
            if opt in visited or opt in walls or opt.y == limit:
                continue
            else:
                queue.append(opt)
    return visited

bottom_height += 2
sand = bfs(sand_origin, walls, bottom_height)
print("Part 2:", len(sand))

