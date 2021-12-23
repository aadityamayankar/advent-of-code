from aocd import get_data, transforms, submit

f = open('input.txt', 'w')
data = get_data(day=3, year=2021)
f.write(data)
lines = transforms.lines(data)
nums = [[row[i] for row in lines] for i in range(len(lines[0]))]

def part_one():
    gamma,epsilon = 0,0
    for i,row in enumerate(nums):
        z,o = row.count('0'), row.count('1')
        if o > z:
            gamma = gamma | (1 << len(nums) - i - 1)

        else:
            epsilon = epsilon | (1 << len(nums) - i - 1)
    return gamma * epsilon

def part_two():
    nums = [[row[i] for row in lines] for i in range(len(lines[0]))]
    _nums = [x[:] for x in nums]
    gamma,epsilon = "",""
    for i,row in enumerate(nums):
        z,o = row.count('0'), row.count('1')
        if z == 0 or o == 0:
            break
        if o >= z:
            zeroes = [x for x,y in enumerate(row) if y == '0']
            for j,x in enumerate(zeroes):
                for y in nums:
                    del y[x-j]
        else:
            ones = [x for x,y in enumerate(row) if y == '1']
            for j,x in enumerate(ones):
                for y in nums:
                    del y[x-j]
    for row in nums:
        gamma += row[0]
    nums = [x[:] for x in _nums]
    for i,row in enumerate(nums):
        z,o = row.count('0'), row.count('1')
        if z == 0 or o == 0:
            break
        if z > o:
            zeroes = [x for x,y in enumerate(row) if y == '0']
            for j,x in enumerate(zeroes):
                for y in nums:
                    del y[x-j]
        else:
            ones = [x for x,y in enumerate(row) if y == '1']
            for j,x in enumerate(ones):
                for y in nums:
                    del y[x-j]
    for row in nums:
        epsilon += row[0]
    return int(gamma,2) * int(epsilon,2)

a, b = part_one(), part_two()

submit(day=3, year=2021, part=1, answer=a)
submit(day=3, year=2021, part=2, answer=b)