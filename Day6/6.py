from aocd import get_data, transforms, submit

f = open('input.txt', 'w')
data = get_data(day=6, year=2021)
f.write(data)

def lanternfish(x):
    dp = [0]*9
    for i in nums:
        dp[i] += 1
    for z in range(x):
        dp = dp[1:7]+[dp[0]+dp[7], dp[8], dp[0]]
    return sum(dp)

nums = map(int,data.split(','))
part_one = lanternfish(80)
nums = map(int,data.split(','))
part_two = lanternfish(256)
print(part_one)
print(part_two)

submit(day=6, year=2021, part=1, answer=part_one)
submit(day=6, year=2021, part=2, answer=part_two)