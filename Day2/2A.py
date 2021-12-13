def solve(instructions):
    x,y = 0,0
    for instruction in instructions:
        dir, val = instruction.split()
        if dir == 'forward':
            x += int(val)
        elif dir == 'down':
            y += int(val)
        else:
            y -= int(val)
    print(y*x)

if __name__ == "__main__":
    f = open("input.txt", "r")
    s = f.read()
    f.close()
    solve(s.split('\n'))