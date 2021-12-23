from aocd import get_data, transforms, submit

f = open('input.txt', 'w')
data = get_data(day=2, year=2021)
f.write(data)

instructions = transforms.lines(data)

def part_one():
    x,y = 0,0
    for instruction in instructions:
        dir, val = instruction.split()
        if dir == 'forward':
            x += int(val)
        elif dir == 'down':
            y += int(val)
        else:
            y -= int(val)
    return y * x

def part_two():
    x,y,aim = 0,0,0
    for instruction in instructions:
        dir, val = instruction.split()
        if dir == 'forward':
            x += int(val)
            y += int(val) * aim
        elif dir == 'down':
            aim += int(val)
        else:
            aim -= int(val)
    return y * x

a, b = part_one(), part_two()

submit(a, part='a', day=2, year=2021)
submit(b, part='b', day=2, year=2021)