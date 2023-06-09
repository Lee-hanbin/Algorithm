# BOJ_21736_silver2-헌내기는친구가필요해

import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

def bfs(start:tuple):
    r, c = start
    que = deque()
    visited = [[0]*m for _ in range(n)]
    que.append((r, c))
    visited[r][c] = 1

    sol = 0
    while que:
        r, c = que.popleft()

        for i in range(4):
            nr = dr[i] + r 
            nc = dc[i] + c
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                visited[nr][nc] = 1
                if map1[nr][nc] == 'X':
                    continue
                que.append((nr, nc))
                if map1[nr][nc] == 'P':
                    sol += 1 
    return sol
n, m = map(int, input().split())

map1 = []
for i in range(n):
    map1.append(input().rstrip())
    for j, e in enumerate(map1[i]):
        if e == "I":
            start = (i, j)

res = bfs(start)

if not res:
    print('TT')
else:
    print(res)