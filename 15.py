import re
from dataclasses import dataclass
from typing import NamedTuple

from aoc import get_input

data = get_input(15).splitlines()
reg = re.compile(r'Sensor at x=(?P<sensor_x>-?\d+), y=(?P<sensor_y>-?\d+): closest beacon is at x=('
                 r'?P<beacon_x>-?\d+), y=(?P<beacon_y>-?\d+)')


class Point(NamedTuple):
    x: int
    y: int

    def distance(self, other: "Point"):
        return abs(self.x - other.x) + abs(self.y - other.y)


@dataclass
class Beacon:
    loc: Point
    nearest: Point


sensors = []
beacons = set()
for line in data:
    match = reg.match(line)
    sensors.append(
        Beacon(
            Point(int(match.group("sensor_x")), int(match.group("sensor_y"))),
            Point(int(match.group("beacon_x")), int(match.group("beacon_y")))
        )
    )
    beacons.add(Point(int(match.group("beacon_x")), int(match.group("beacon_y"))))


def check_line(target):
    ranges_covered = []
    for sensor in sensors:
        dis_to_beacon = sensor.loc.distance(sensor.nearest)
        dis_to_target_line = sensor.loc.distance(Point(sensor.loc.x, y=target))
        if dis_to_target_line > dis_to_beacon:
            continue
        else:
            leftover = abs(dis_to_target_line - dis_to_beacon)
            if leftover == 0:
                ranges_covered.append(range(sensor.loc.x, sensor.loc.x + 1))
            else:
                ranges_covered.append(range(sensor.loc.x - leftover, sensor.loc.x + leftover + 1))

    ranges_covered.sort(key=lambda x: x.start)

    new_ranges = []
    if ranges_covered:
        r = ranges_covered.pop(0)
        while ranges_covered:
            next_r = ranges_covered.pop(0)
            if r.stop >= next_r.start:
                r = range(r.start, max(r.stop, next_r.stop))
            else:
                new_ranges.append(r)
                r = next_r
        new_ranges.append(r)
        return new_ranges
    else:
        return []


part1 = len(check_line(2000000)[0])
for beacon in beacons:
    if beacon.y == 2000000:
        part1 -= 1
print('Part 1:', part1)

for line in range(4_000_000):
    ranges = check_line(line)
    if len(ranges) > 1:
        print('Part 2:', ranges[0].stop * 4_000_000 + line)
        break
    elif line % 100000 == 0:
        print(line)
