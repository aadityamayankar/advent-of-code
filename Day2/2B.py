def solve(instructions):
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
    print(y*x)

if __name__ == "__main__":
    f = open("input.txt", "r")
    s = f.read()
    f.close()
    solve(s.split('\n'))