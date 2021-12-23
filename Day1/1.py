from aocd import get_data, transforms, submit

f = open('input.txt','w')
data = get_data(day=1, year=2021)
f.write(data)
nums = transforms.numbers(data)
def part_one():
    cnt = 0
    for i in range(1,len(nums),1):
        if nums[i] > nums[i-1]:
            cnt += 1
    return cnt

def part_two():
    l = []
    for i in range(3,len(nums)+1,1):
        l.append(sum(nums[i-3:i]))
    cnt = 0
    for i in range(1,len(l),1):
        if l[i] > l[i-1]:
            cnt += 1
    return cnt

a, b = part_one(), part_two()

submit(a, part='a', day=1, year=2021)
submit(b, part='b', day=1, year=2021)