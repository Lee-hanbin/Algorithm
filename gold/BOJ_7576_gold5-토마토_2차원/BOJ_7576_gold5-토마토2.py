# BOJ_7576_gold5-토마토

import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

def bfs():
    que = deque()
    for r, c in tomato_idx_box:
        que.append((r, c, 1))
    while que:
        r, c, cnt = que.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nr < n and 0 <= nc < m and store_box[nr][nc] == 0:
                que.append((nr, nc, cnt+1))
                store_box[nr][nc] = cnt + 1


m, n = map(int, input().split())

tomato_idx_box = set()

store_box = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if store_box[i][j] == 1:
            tomato_idx_box.add((i,j))

bfs()
sol = 0
for i in store_box:
    chk = max(i)
    if sol < chk:
        sol = chk
    for j in i:
        if j == 0:
            print(-1)
            exit()
print(sol - 1)