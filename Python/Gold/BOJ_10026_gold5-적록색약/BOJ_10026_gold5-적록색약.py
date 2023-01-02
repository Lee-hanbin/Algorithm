# BOJ_10026_gold5-적록색약

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

# 일반인
def dfs(idx):
    r, c = idx
    color = map1[r][c]
    visited_A.add((r,c))
    for i in range(4):
        nr = dr[i] + r
        nc = dc[i] + c
        if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visited_A and map1[nr][nc] == color:
            dfs((nr,nc))

# 적록색약
def dfs_rg(idx):
    r, c = idx
    color = map1[r][c]
    if color == 'R' or color == 'G':
        color = 'RG'
    visited_RG.add((r,c))
    for i in range(4):
        nr = dr[i] + r
        nc = dc[i] + c
        if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visited_RG and map1[nr][nc] in color:
            dfs_rg((nr,nc))

n = int(input())

map1 = [list(input().rstrip()) for _ in range(n)]

visited_A = set()
visited_RG = set()

cnt_A = 0
cnt_RG = 0

for i in range(n):
    for j in range(n):
        # 일반인
        if (i,j) not in visited_A:
            cnt_A += 1
            dfs((i,j))
        # 적록색약
        if (i,j) not in visited_RG:
            cnt_RG += 1
            dfs_rg((i,j))

print(cnt_A, cnt_RG)