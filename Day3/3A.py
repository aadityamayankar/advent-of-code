def solve(nums):
    nums = [[row[i] for row in nums] for i in range(len(nums[0]))]
    gamma,epsilon = 0,0
    for i,row in enumerate(nums):
        z,o = row.count('0'), row.count('1')
        if o > z:
            gamma = gamma | (1 << len(nums) - i - 1)

        else:
            epsilon = epsilon | (1 << len(nums) - i - 1)
    print(gamma * epsilon)

if __name__ == "__main__":
    f = open("input.txt", "r")
    s = f.read()
    f.close()
    solve(s.split('\n'))