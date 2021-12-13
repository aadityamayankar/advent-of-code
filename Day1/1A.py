def solve(nums):
    cnt = 0
    for i in range(1,len(nums),1):
        if nums[i] > nums[i-1]:
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    f = open("input.txt", mode='r')
    s = f.read()
    f.close()
    solve(list(map(int,s.split('\n'))))