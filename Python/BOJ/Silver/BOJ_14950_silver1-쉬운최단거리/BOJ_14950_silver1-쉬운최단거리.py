# BOJ_14950_silver1-쉬운최단거리

import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

def bfs(start:tuple):
    r, c = start
    que = deque()
    que.append((r, c, 0))
    visited[r][c] = 0
    while que:
        r, c, cnt = que.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nr < n and 0 <= nc < m and map1[nr][nc] and visited[nr][nc] < 0:
                visited[nr][nc] = cnt + 1
                que.append((nr, nc, cnt+1))
    
    return visited


n, m = map(int, input().split())

map1 = []
visited = [[-1]*m for _ in range(n)]

for i in range(n):
    map1.append(list(map(int, input().split())))
    for j, e in enumerate(map1[i]):
        if e == 2:
            start = (i, j)
            continue
        if e == 0:
            visited[i][j] = 0

bfs(start)

for i in visited:
    print(*i)