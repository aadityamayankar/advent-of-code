def solve(nums):
    l = []
    for i in range(3,len(nums)+1,1):
        l.append(sum(nums[i-3:i]))
    cnt = 0
    for i in range(1,len(l),1):
        if l[i] > l[i-1]:
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    f = open("input.txt", mode='r')
    s = f.read()
    f.close()
    solve(list(map(int,s.split('\n'))))