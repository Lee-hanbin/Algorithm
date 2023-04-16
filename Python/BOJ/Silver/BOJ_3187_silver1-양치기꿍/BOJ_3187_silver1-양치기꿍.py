# BOJ_3187_silver1-양치기꿍

import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]


def bfs(s, w):
    # 양과 늑대를 모두 체크
    while set_sheep or set_wolf:
        if set_sheep:               # 양이 존재하면 양 넣기
            r, c = set_sheep.pop()
            sheep_cnt = 1
            wolf_cnt = 0
        else:                       # 양이 없으면 늑대 넣기
            r, c = set_wolf.pop()
            wolf_cnt = 1
            sheep_cnt = 0
        que = deque()
        visited = set()
        que.append((r, c))          # 큐에 넣기
        visited.add((r, c))    
        while que:  
            r, c = que.popleft()
            # delta search
            for i in range(4):
                nr = dr[i] + r
                nc = dc[i] + c
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    if map1[nr][nc] == '#':         # 울타리면 pass
                        continue
                    elif map1[nr][nc] == 'k':       # 양이면 양 카운팅 후, set에서 빼기
                        sheep_cnt += 1
                        set_sheep.discard((nr, nc))
                    elif map1[nr][nc] == 'v':       # 늑대면 늑대 카운팅 후, set에서 빼기
                        wolf_cnt += 1
                        set_wolf.discard((nr, nc))
                    que.append((nr, nc))            # 큐에 담기

        if sheep_cnt > wolf_cnt:        # 양이 더 많으면 늑대 잡아먹기 (양만 카운팅)
            s += sheep_cnt
        else:                           # 늑대가 더 많으면 양 잡아먹기 (늑대만 카운팅)
            w += wolf_cnt

    return s, w


n, m = map(int, input().split())

map1 = []
set_wolf = set()
set_sheep = set()
total_wolf_cnt = 0
total_sheep_cnt = 0

# 양의 인덱스와 늑대의 인덱스를 set에 담기
for i in range(n):
    map1.append(list(input().rstrip()))
    for j, e in enumerate(map1[i]):
        if e == 'k':
            set_sheep.add((i, j))
        elif e == 'v':
            set_wolf.add((i, j))

print(*bfs(total_sheep_cnt, total_wolf_cnt))

