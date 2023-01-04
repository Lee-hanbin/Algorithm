# BOJ_16236_gold3_아기상어

import sys
from collections import deque, defaultdict

input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [ 0,-1, 0, 1]

def bfs(idx, level):
    global shark_age

    i, j = idx
    que = deque()
    visited = set()
    chk_lst_idx = []
    chk = float('inf')

    visited.add((i,j))
    que.append((i, j, 0))

    while que:
        r, c, time = que.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visited and map1[nr][nc] <= shark_age:
                if 0 < map1[nr][nc] <= level:
                    visited.add((nr, nc))
                    if chk >= time:             # 같은 시간이 걸리는 먹을 물고기 리스트에 담기
                        chk = time
                        chk_lst_idx.append((nr, nc, time + 1))
                        continue
                if map1[nr][nc] == shark_age or map1[nr][nc] == 0:  # 물고기와 상어의 크기가 같거나 물고기가 없으면 append
                    que.append((nr, nc, time + 1))
                    visited.add((nr, nc))

    if chk_lst_idx:         # 먹을 물고기가 존쟇하면
        chk_lst_idx = sorted( chk_lst_idx, key= lambda x : (x[0], x[1]))    # 가장 윗쪽에 가장 왼쪽
        r, c, time = chk_lst_idx[0]
        map1[r][c] = 0      # 먹은 물고기는 map 갱신
        return r, c, time
    else:                   # 더이상 찾을 수 없으면 r = -1 반환
        return -1, -1, 0


n = int(input())

map1 = [list(map(int, input().split())) for _ in range(n)]

# 아기상어 시작위치 찾기
for i in range(n):
    def start_chk_idx(i):
        for j in range(n):
            if map1[i][j] == 9:
                map1[i][j] = 0
                return (i,j)
        return 0
    start_idx = start_chk_idx(i)
    if start_idx:
        break

r, c = start_idx
shark_age = 2
count = 0
time = 0

while r > -1:
    r, c, chk_time = bfs(start_idx, shark_age - 1)
    if chk_time:                # 값이 존재하면
        count += 1              # level up을 위한 경험치 
        if count == shark_age:  # 경험치가 꽉 차면 level up
            count = 0           # 경험치 초기화
            shark_age += 1      # level up
    time += chk_time            # 시간 갱신
    start_idx = r, c            # 시작점 갱신
print(time)