# BOJ_2737_silver1-버섯농장

import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(100000)

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

def dfs(r, c):
    global cnt
    for i in range(4):
        nr =dr[i] + r
        nc =dc[i] + c
        if 0 <= nr < n and 0 <= nc < n and not farm[nr][nc]:
            cnt += 1
            farm[nr][nc] = 1
            dfs(nr, nc)


n, m, k = map(int, input().split())

farm = list(list(map(int, input().split())) for _ in range(n))

zero_box = []

# 버섯을 심을 수 있는 영역의 수와 버섯의 개수 체크
for r in range(n):
    for c in range(n):
        if not farm[r][c]:
            cnt = 1
            farm[r][c] = 1
            dfs(r, c)
            zero_box.append(cnt)

if not zero_box:
    print("IMPOSSIBLE")
    exit()

area_cnt = len(zero_box)
if area_cnt > m:
    print("IMPOSSIBLE")
else:
    zero_box.sort(reverse=True)
    area_size = 0
    cnt = 0
    while zero_box and cnt < m :
        if not area_size:
            area_size = zero_box.pop()
        chk = area_size // k
        if area_size % k:
            chk += 1
        cnt += chk
        area_size = 0

    if zero_box or m < cnt:
        print("IMPOSSIBLE")
    else:
        print("POSSIBLE")
        print( m - cnt )

