from typing import NamedTuple, List
from string import ascii_lowercase
from aoc import get_input

data = get_input(12).splitlines()


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other: "Point"):
        return Point(self.x + other.x, self.y + other.y)


area = []
for y, line in enumerate(data):
    map_line = []
    for x, c in enumerate(line):
        if c == 'S':
            start = Point(x, y)
            map_line.append(0)
        elif c == 'E':
            end = Point(x, y)
            map_line.append(ascii_lowercase.index('z'))
        else:
            map_line.append(ascii_lowercase.index(c))
    area.append(map_line)


def bfs(area: List[List[int]], start: Point, end: Point):
    visted = set()
    queue = list()
    queue.append((start, [start]))
    while queue:
        loc, path = queue.pop(0)
        height = area[loc.y][loc.x] + 1
        for direction in [Point(0,1), Point(1,0), Point(-1, 0), Point(0, -1)]:
            step = loc + direction
            if step.x not in range(len(area[0])) or step.y not in range(len(area)):
                continue
            dest = area[step.y][step.x]
            if step == end and dest <= height:
                return path+[end]
            if step not in visted and dest <= height:
                queue.append((step, path + [step]))
                visted.add(step)


def bfs2(area: List[List[int]], start: Point):
    visted = set()
    queue = list()
    queue.append((start, set()))
    while queue:
        loc, path = queue.pop(0)
        height = area[loc.y][loc.x] - 1
        for direction in [Point(0,1), Point(1,0), Point(-1, 0), Point(0, -1)]:
            step = loc + direction
            if step.x not in range(len(area[0])) or step.y not in range(len(area)):
                continue
            dest = area[step.y][step.x]
            if height == -1 and dest >= height:
                return path|{end}
            if step not in visted and dest >= height:
                queue.append((step, path | {step}))
                visted.add(step)


part1 = bfs(area, start, end)
print("Part 1:", len(part1)-1)
part2 = bfs2(area, end)
print("Part 2:", len(part2)-1)
