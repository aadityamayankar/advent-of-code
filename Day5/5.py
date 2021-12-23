from aocd import get_data, transforms, submit
from math import inf

f = open('input.txt', 'w')
data = get_data(day=5, year=2021)
f.write(data)
points = transforms.lines(data)
mx = 0
for point in points:
    a,b = point.split(' -> ')
    x1,y1 = int(a.split(',')[0]),int(a.split(',')[1])
    x2,y2 = int(b.split(',')[0]),int(b.split(',')[1])
    mx = max(mx,x1,y1,x2,y2)

def slope(x1,x2,y1,y2):
    if x1 == x2:
        return 0
    elif y1 == y2:
        return inf
    else:
        return (y2-y1)/(x2-x1)

def count(grid):
    cnt = 0
    for i in grid:
        for j in i:
            if j > 1:
                cnt += 1
    return cnt

def part_one():
    grid = [[0 for _ in range(mx+1)] for _ in range(mx+1)]
    for point in points:
        a,b = point.split(' -> ')
        x1,y1 = int(a.split(',')[0]),int(a.split(',')[1])
        x2,y2 = int(b.split(',')[0]),int(b.split(',')[1])
        m = slope(x1, x2, y1, y2)
        if m == 0:
            for i in range(min(y1,y2),max(y2,y1)+1):
                grid[i][x1] += 1
        if m == inf:
            for i in range(min(x1,x2),max(x2,x1)+1):
                grid[y1][i] += 1
    return count(grid)

def part_two():
    grid = [[0 for _ in range(mx+1)] for _ in range(mx+1)]
    for point in points:
        a,b = point.split(' -> ')
        x1,y1 = int(a.split(',')[0]),int(a.split(',')[1])
        x2,y2 = int(b.split(',')[0]),int(b.split(',')[1])
        m = slope(x1, x2, y1, y2)
        if m == 0:
            for i in range(min(y1,y2),max(y2,y1)+1):
                grid[i][x1] += 1
        elif m == inf:
            for i in range(min(x1,x2),max(x2,x1)+1):
                grid[y1][i] += 1
        elif m == 1.0:
            a,b = min(x1,x2),max(x1,x2)
            c,d = min(y1,y2),max(y1,y2)
            while b >= a and d >= c:
                grid[c][a] += 1
                a += 1
                c += 1
        elif m == -1.0:
            a,b = min(x1,x2),max(x1,x2)
            c,d = min(y1,y2),max(y1,y2)
            while b >= a and d >= c:
                grid[d][a] += 1
                a += 1
                d -= 1
    return count(grid)

a = part_one()
grid = [[0 for _ in range(mx+1)] for _ in range(mx+1)]
b = part_two()

submit(day=5, year=2021, part=1, answer=a)
submit(day=5, year=2021, part=2, answer=b)