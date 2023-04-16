# BOJ_1987_gold4-알파벳

import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]


def bfs():
    sol = 1
    visited = map1[0][0]
    set_list = {(0, 0, visited)}
    while set_list:
        r, c, chk_str = set_list.pop()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nr < R and 0 <= nc < C and map1[nr][nc] not in chk_str:
                set_list.add((nr, nc, chk_str + map1[nr][nc]))
                sol = max(sol, len(chk_str)+1)
    return sol

R, C = map(int, input().split())

map1 = [list(input().rstrip()) for _ in range(R)]

print(bfs())

# def bfs():
#     sol = 0
#     que = deque()
#     visited = set(map1[0][0])
#     que.append((0, 0, visited))
#     while que:
#         r, c, chk_set = que.popleft()
#         cnt = 0
#         for i in range(4):
#             nr = dr[i] + r
#             nc = dc[i] + c
#             if 0 <= nr < R and 0 <= nc < C and map1[nr][nc] not in chk_set:
#                 cnt += 1
#                 que.append((nr, nc, chk_set | set(map1[nr][nc])))
#         if not cnt:
#              sol = max(sol, len(chk_set))
#     return sol

# R, C = map(int, input().split())

# map1 = [list(input().rstrip()) for _ in range(R)]

# print(bfs())