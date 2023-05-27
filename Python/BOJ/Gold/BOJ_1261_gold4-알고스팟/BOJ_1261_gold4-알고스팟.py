# BOJ_1261_gold4-알고스팟

import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

#1. 0-1 bfs
def bfs(start_row, start_col):
    que = deque()
    cost[start_row][start_col] = 0
    que.append((start_row, start_col))
    while que:
        r, c = que.popleft()

        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nr < n and 0 <= nc < m and  cost[nr][nc] == -1:
                if not map1[nr][nc]:
                    cost[nr][nc] = cost[r][c]
                    que.appendleft((nr, nc))
                else:
                    cost[nr][nc] = cost[r][c] + 1
                    que.append((nr, nc))

    return cost[n-1][m-1]

from heapq import heapify, heappush, heappop

#2. dijkstra
def dijkstra():
    distance = list([float('inf')] * m for _ in range(n))
    distance[0][0] = 0

    hq = []
    heappush(hq, (0, 0, 0))

    while hq:
        w, r, c = heappop(hq)

        if w <= distance[r][c]:
            for i in range(4):
                nr = dr[i] + r
                nc = dc[i] + c
                if 0 <= nr < n and 0 <= nc < m:
                    if w + map1[nr][nc] < distance[nr][nc]:
                        distance[nr][nc] = w + map1[nr][nc]
                        heappush(hq, (distance[nr][nc], nr, nc))
    return distance[n-1][m-1]

m, n = map(int, input().split())

map1 = list(list(map(int, input().rstrip())) for _ in range(n))
cost = [[-1]* m for _ in range(n)]

print(bfs(0, 0))
print(dijkstra())

