# BOJ_7579_gold5-토마토_3차원

import sys
from collections import deque

input = sys.stdin.readline

dt = [-1, 1, 0, 0, 0, 0]
dr = [ 0, 0,-1, 1, 0, 0]
dc = [ 0, 0, 0, 0,-1, 1]

def bfs():
    que = deque()
    for t, r, c in tomato_idx_box:
        que.append((t, r, c, 1))
    while que:
        t, r, c, cnt = que.popleft()
        for i in range(6):
            nt = dt[i] + t
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nt < h and 0 <= nr < n and 0 <= nc < m and store_box[nt][nr][nc] == 0:
                que.append((nt, nr, nc, cnt + 1))
                store_box[nt][nr][nc] = cnt + 1


m, n, h = map(int, input().split())

store_box = []
tomato_idx_box = set()

for t in range(h):
    store_box.append([list(map(int, input().split())) for _ in range(n)])
    for r in range(n):
        for c in range(m):
            if store_box[t][r][c] == 1:
                tomato_idx_box.add((t,r,c))

bfs()

sol = 0
for i in store_box:
    for j in i:
        chk = max(j)
        if sol < chk:
            sol = chk
        for k in j:
            if k == 0:
                print(-1)
                exit()

print(sol - 1)