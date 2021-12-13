def solve(nums):
    nums = [[row[i] for row in nums] for i in range(len(nums[0]))]
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
    print(int(gamma,2) * int(epsilon,2))


if __name__ == "__main__":
    f = open("input.txt", "r")
    s = f.read()
    f.close()
    solve(s.split('\n'))