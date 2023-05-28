# BOJ_2665-gold4-미로만들기

import sys
from collections import deque
from heapq import heapify, heappush, heappop

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

#1. 0-1 bfs
def bfs():
    que = deque()
    cost =[[-1]*n for _ in range(n)]
    cost[0][0] = 0
    que.append((0, 0))
    while que:
        r, c = que.popleft()

        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nr < n and 0 <= nc < n and cost[nr][nc] < 0:
                if map1[nr][nc] == "1":
                    cost[nr][nc] = cost[r][c]
                    que.appendleft((nr, nc))
                else:
                    cost[nr][nc] = cost[r][c] + 1
                    que.append((nr, nc))
    return cost[n-1][n-1]

#2. dijkstra 
def dijkstra():
    distance = list([float('inf')] * n for _ in range(n))
    distance[0][0] = 0

    hq = []
    heappush(hq, (0, 0, 0))

    while hq:
        w, r, c = heappop(hq)

        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nr < n and 0 <= nc < n:
                if w + (int(map1[nr][nc]) + 1) % 2 < distance[nr][nc]:
                    distance[nr][nc] = w + (int(map1[nr][nc]) + 1) % 2
                    heappush(hq, (distance[nr][nc], nr, nc))
    return distance[n-1][n-1]

n = int(input())

map1 = list(input().rstrip() for _ in range(n))


print(bfs())
print(dijkstra())