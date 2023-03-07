# BOJ_9763_silver1-마을의친밀도

import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]

d = [6000] * n 
sol = 6000
for i in range(n-1):
    for j in range(i+1, n):
        distance = abs(lst[i][0] - lst[j][0]) + abs(lst[i][1]- lst[j][1]) + abs(lst[i][2] - lst[j][2])
        sol = min(sol, min(d[i], d[j])+distance)
        d[i] = min(d[i], distance)
        d[j] = min(d[j], distance)
print(sol)
#1. N^3...
# sol = 6000
# for i in combinations(lst, 3):
#     d12 = abs(i[0][0] - i[1][0]) + abs(i[0][1]- i[1][1]) + abs(i[0][2] - i[1][2])
#     d23 = abs(i[1][0] - i[2][0]) + abs(i[1][1]- i[2][1]) + abs(i[1][2] - i[2][2])
#     sol = min(sol, d12 + d23)

# print(sol)