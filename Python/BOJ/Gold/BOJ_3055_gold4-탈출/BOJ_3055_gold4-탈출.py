# BOJ_3055_gold4-탈출

import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

def bfs(idx):
    s_r, s_c = idx
    que = deque()
    visited_water = set()               # 물 방문표시
    visited_urchin = set()              # 고슴도치 방문표시

    # 물을 먼저 큐에 넣기
    for i, j in water_lst:
        que.append((i, j, 'w'))
        visited_water.add(i)
    
    # 고슴도치를 큐에 넣기 
    que.append((s_r, s_c, 0))
    visited_urchin.add((s_r, s_c))

    while que:
        r, c, cnt = que.popleft()

        # 1. 물 먼저 큐에 넣기
        if cnt == 'w':
            for i in range(4):
                nr = dr[i] + r
                nc = dc[i] + c
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited_water:
                    if map1[nr][nc] == ".":         # 빈 칸이면
                        que.append((nr, nc, cnt))
                        visited_water.add((nr, nc))
        # 2. 고슴도치 큐에 넣기
        else:
            for i in range(4):
                nr = dr[i] + r
                nc = dc[i] + c
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited_water and (nr, nc) not in visited_urchin:
                    if map1[nr][nc] == ".":             # 빈칸이면 큐에 넣기
                        que.append((nr, nc, cnt+1))
                        visited_urchin.add((nr, nc))
                    elif map1[nr][nc] == "D":           # 비버 굴이면 반환
                        return cnt + 1
    return 'KAKTUS'

R, C =map(int, input().split())

water_lst = []
map1 = []
for i in range(R):
    map1.append(list(input().rstrip()))
    for j, e in enumerate(map1[i]):
        if e == "*":
            water_lst.append((i, j))
        elif e == "S":
            map1[i][j] = '.'
            urchin_start = (i, j)


print(bfs(urchin_start))