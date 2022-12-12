from aoc import get_input

data = get_input(10).splitlines()

screen = ['.'] * 240
part1 = 0
cycle = 0
reg = 1
adding = False
to_add = 0
while cycle < 240:
    if cycle%40 in range(reg-1, reg+2):
        screen[cycle] = '#'
    cycle += 1
    if cycle in {20, 60, 100, 140, 180, 220}:
        part1 += cycle * reg

    if adding:
        reg += to_add
        adding = False
    else:
        if data:
            inst = data.pop(0)
        else:
            inst = 'noop'
        if inst.startswith("addx"):
            to_add = int(inst.split()[1])
            adding = True
print(part1)
print(''.join(screen[:40]))
print(''.join(screen[40:80]))
print(''.join(screen[80:120]))
print(''.join(screen[120:160]))
print(''.join(screen[160:200]))
print(''.join(screen[200:240]))
