# BOJ_2206_gold3-벽 부수고 이동하기

import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

def bfs():
    que = deque()
    visited = set()
    que.append((0, 0, 1, False))
    visited.add((0, 0, False))
    while que:
        r, c, cnt, switch = que.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nr < n and 0 <= nc < m and (nr, nc, switch) not in visited:
                if (nr, nc) == (n-1, m-1):
                    return cnt + 1
                if map1[nr][nc] == '0':
                    que.append((nr, nc, cnt + 1, switch))
                    visited.add((nr, nc, switch))
                else:
                    if switch == False and (nr, nc) in wall_idx_set:                    
                        que.append((nr, nc, cnt + 1, True))
                        wall_idx_set.discard((nr, nc))
                        visited.add((nr, nc, True))
    return -1


n, m = map(int, input().split())

map1 = []
wall_idx_set = set()

if n == 1 and m == 1:
    print(1)
    exit()

for i in range(n):
    map1.append(list(input().rstrip()))
    for j, e in enumerate(map1[i]):
        if e == '1':
            wall_idx_set.add((i, j))

print(bfs())
