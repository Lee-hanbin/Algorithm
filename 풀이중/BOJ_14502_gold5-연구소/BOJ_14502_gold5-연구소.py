# BOJ_14502_gold5-연구소

import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

def bfs():
    que = deque()
    while visited:
        v = visited.pop()
        que.append(v)
        while que:
            r, c = que.popleft()
            for i in range(4):
                nr = dr[i] + r
                nc = dc[i] + c
                # 0인 곳을 탐색하는데 해당 탐색 위치의 


n, m = map(int, input().split())
lst = [list(map(int,input().split())) for _ in range(n)]

# 0: 빈칸
# 1: 벽
# 2: 바이러스

visited = set()

for i in range(n):
    for j in range(m):
        if lst[i][j] == 2:
            visited.add((i,j))


bfs()