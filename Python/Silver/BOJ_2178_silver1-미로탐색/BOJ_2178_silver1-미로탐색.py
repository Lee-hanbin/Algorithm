# BOJ_2178_silver1-미로탐색.py

import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

def bfs(idx):
    que = deque()
    visited = set()
    visited.add((idx[0], idx[1]))
    que.append((idx[0], idx[1] , 1))
    while que:
        r, c, cnt = que.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
                if map1[nr][nc] == 1:
                    visited.add((nr, nc))
                    if nr == n -1 and nc == m -1:
                        return cnt + 1
                    que.append((nr, nc, cnt+1))

n, m = map(int, input().split())

map1 = [list(map(int, input().rstrip())) for _ in range(n)]


print(bfs((0, 0)))