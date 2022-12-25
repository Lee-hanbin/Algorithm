# BOJ_1992_silver1-쿼드트리

import sys

input = sys.stdin.readline

def rec_f(idx, num):
    r, c = idx
    sol.append('(')
    
    if num == 2:
        sum_submap = map1[r][c] + map1[r+1][c] + map1[r][c+1] + map1[r+1][c+1]
        if sum_submap == 4:
            sol.append(1)
        elif sum_submap == 0:
            sol.append(0)
        else:
            for i in [(r, c), (r, c+1), (r+1, c), (r+1, c+1)]:        
                sol.append(map1[i[0]][i[1]])
    else:
        num = num // 2
        for i in [(r, c), (r, c + num), (r + num, c), (r + num, c + num)]:
            sum_submap = 0
            for j in range(i[0], i[0] + num):
                sum_submap += sum(map1[j][i[1]:i[1] + num])
            if sum_submap == num**2:
                sol.append(1)
            elif sum_submap == 0:
                sol.append(0)
            else:
                # print(i, num // 2)
                rec_f(i, num)

    sol.append(')')

n = int(input())
map1 = [list(map(int, input().rstrip())) for _ in range(n)]
sol = []

sum_map = 0
for i in map1:
    sum_map += sum(i)
if sum_map == n ** 2:
    sol.append(1)
elif sum_map == 0:
    sol.append(0)
else:
    rec_f((0, 0), n)

for i in sol:
    print(i, end='')