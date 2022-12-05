from collections import defaultdict

from aoc import get_input

data = get_input(5).splitlines()

crates = defaultdict(list)
setup_done = False
for line in data:

    if not setup_done:

        stacks = [line[i:i + 3] for i in range(0, len(line), 4)]
        if not stacks:
            setup_done = True
            for val in crates.values():
                val.reverse()
            continue
        if '[' not in line:
            continue
        for i, stack in enumerate(stacks):
            if stack.strip():
                crates[i+1].append(stack[1])
    else:
        line_sp = line.split()
        quantity, from_c, to_c = int(line_sp[1]), int(line_sp[3]), int(line_sp[5])
        for _ in range(quantity):
            crates[to_c].append(crates[from_c].pop())
print("Part 1:", "".join([crates[x+1][-1] for x in range(len(crates))]))

crates = defaultdict(list)
setup_done = False
for line in data:

    if not setup_done:

        stacks = [line[i:i + 3] for i in range(0, len(line), 4)]
        if not stacks:
            setup_done = True
            for val in crates.values():
                val.reverse()
            continue
        if '[' not in line:
            continue
        for i, stack in enumerate(stacks):
            if stack.strip():
                crates[i+1].append(stack[1])
    else:
        line_sp = line.split()
        quantity, from_c, to_c = int(line_sp[1]), int(line_sp[3]), int(line_sp[5])
        crates[to_c].extend(crates[from_c][-quantity:])
        crates[from_c]=crates[from_c][:-quantity]
print("Part 2:", "".join([crates[x+1][-1] for x in range(len(crates))]))