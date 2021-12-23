from aocd import get_data, transforms, submit

f = open('input.txt', 'w')
data = get_data(day=7, year=2021)
f.write(data)

def part_one():
    lo, hi = min(nums), max(nums)
    def fuelCost(target):
        return sum(abs(target-pos) for pos in nums)
    while lo < hi:
        mid = (lo + hi + 1) >> 1
        if fuelCost(mid) < fuelCost(mid-1):
            lo = mid
        else:
            hi = mid - 1
    return fuelCost(lo)

def part_two():
    hi, lo = max(nums), min(nums)
    def fuelCost(target):
        return sum(abs(target-pos)*(abs(target-pos)+1)//2 for pos in nums)
    while lo < hi:
        mid = (lo + hi + 1) >> 1
        if fuelCost(mid) < fuelCost(mid-1):
            lo = mid
        else:
            hi = mid - 1
    return fuelCost(lo)

nums = list(map(int,data.split(',')))   
print(part_one())
print(part_two())

submit(day=7, year=2021, part=1, answer=part_one())
submit(day=7, year=2021, part=2, answer=part_two())