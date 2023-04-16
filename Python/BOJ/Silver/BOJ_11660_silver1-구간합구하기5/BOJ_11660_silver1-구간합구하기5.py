# BOJ_11660_silver1-구간합구하기5

import sys
from pprint import pprint

input = sys.stdin.readline

n, m = map(int,input().split())

map1 = [list(map(int,input().split())) for _ in range(n)]
cul_map = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        cul_map[i+1][j+1] = map1[i][j] + cul_map[i+1][j] + cul_map[i][j+1] - cul_map[i][j] 


for i in range(m):
    r1, c1, r2, c2 = map(int,input().split())
    if r1 > r2:
        r1, r2 = r2, r1
    if c1 > c2:
        c1, c2 = c2, c1
    print(cul_map[r2][c2] - cul_map[r2][c1-1] - cul_map[r1-1][c2] + cul_map[r1-1][c1-1])
