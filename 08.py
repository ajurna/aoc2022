from aoc import get_input

data = [list(map(int, line)) for line in get_input(8).splitlines()]
data_flip = [list(z) for z in zip(*data)]


def check_los(seq: list, max_height: int):
    distance = 0
    while seq:
        height = seq.pop(0)
        distance += 1
        if height >= max_height:
            return distance
    return distance


part1 = 0
part2 = 0
for y in range(len(data)):
    for x in range(len(data_flip)):
        val = data[y][x]
        if max(data[y][:x] + [-1]) < val or max(data[y][x + 1:] + [-1]) < val or max(
                data_flip[x][:y] + [-1]) < val or max(data_flip[x][y + 1:] + [-1]) < val:
            part1 += 1

        if (new_part2 := check_los(data_flip[x][y::-1][1:], val) * check_los(data_flip[x][y + 1:], val) * check_los(
                data[y][x + 1:], val) * check_los(data[y][x::-1][1:], val)) > part2:
            part2 = new_part2

print("Part 1:", part1)
print("Part 2:", part2)
