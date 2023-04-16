# BOJ_17142_gold3-연구소3

import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

def bfs():
    que = deque()
    visited = set()

    # 터뜨린 바이러스 공간 0으로 초기화
    map_chk = deepcopy(map1)
    for r, c in f_virus:
        map_chk[r][c] = 0
        que.append((r, c, 0))
        visited.add((r,c))

    # 바이러스 퍼뜨리기
    while que:
        r, c, cnt = que.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                if  map_chk[nr][nc] == 0:                       # 빈 공간인 경우, 퍼뜨리기
                    que.append((nr, nc, cnt + 1))
                    visited.add((nr, nc))
                elif map_chk[nr][nc] == -1:                     # 비활성 바이러스인 경우
                    if len(set(virus)|visited) + wall_cnt == n*n:    # 이미 퍼진 경우, pass
                        visited.add((nr,nc))
                    else:                                       # 아직 안 퍼진 경우, 활성화 
                        visited.add((nr,nc))
                        que.append((nr, nc, cnt + 1))
    visited = visited|set(virus)
    
    if len(visited) + wall_cnt == n*n:
        return cnt
    else:
        return -1




n, m = map(int, input().split())

sol = []
map1 = []
virus = []
wall_cnt = 0

# 연구소를 입력 받으면서 바이러스 위치와 벽의 위치를 체크
for i in range(n):
    map1.append(list(map(int, input().split())))
    for j, e in enumerate(map1[i]):
        if e == 2:
            map1[i][j] = -1         # 비활성 바이러스 체크를 위해 -1로 갱신
            virus.append((i,j)) 
        elif e == 1:
            wall_cnt += 1

# 바이러스가 초기에 다 퍼져있는 경우
if len(virus) + wall_cnt == n*n:
    print(0)
    exit()

# 터뜨릴 바이러스 m개 고르기
for i in combinations(virus, m):
    f_virus = list(i)
    chk = bfs()
    if chk > -1:
        sol.append(chk)

# 최소값 출력
if sol:
    print(min(sol))
else:
    print(-1)

