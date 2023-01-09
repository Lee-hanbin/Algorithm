# BOJ_1799_gold1-비숍

import sys

input = sys.stdin.readline

def dfs(idx):
    visited[idx] = True
    l = link[idx]
    for p in l:
        if r2l[p] == 0 or (not visited[r2l[p]] and dfs(r2l[p])):
            r2l[p] = idx
            l2r[idx] = p
            return True
    return False

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
right = [[0] * n for _ in range(n)]
left = [[0] * n for _ in range(n)]
r, l = 1, 1

# 우하단
for j in range(n):
    i = 0
    while i<n and 0<=j:
        if table[i][j] == 1:
            right[i][j] = r
        i += 1; j -= 1
    r += 1

# 좌하단
for i in range(1, n):
    j = n-1
    while i<n and 0<=j:
        if table[i][j] == 1:
            right[i][j] = r
        i += 1; j -= 1
    r += 1

# 좌상단
for j in range(n-1, -1, -1):
    i = 0
    while i<n and j<n:
        if table[i][j] == 1:
            left[i][j] = l
        i += 1; j += 1
    l += 1

# 우상단
for i in range(1, n):
    j = 0
    while i<n and j<n:
        if table[i][j] == 1:
            left[i][j] = l
        i += 1; j += 1
    l += 1

# 1<= l, r <=2*n
link = [[] for _ in range(l)]
for i in range(n):
    for j in range(n):
        if table[i][j]:
            link[left[i][j]].append(right[i][j])


l2r = [0] * (2*n)
r2l = [0] * (2*n)
ans = 0
for i in range(1, 2*n):
    visited = [False] * (2*n)
    if dfs(i):
        ans += 1
print(ans)

# #   좌상, 우상, 좌하, 우하
# dr = [-1,-1, 1, 1]
# dc = [-1, 1,-1, 1]

# def bfs(f_r, f_c):
#     cnt = 1
#     set_chk = set()
#     set_move = set()
#     set_chk = set_idx|set_chk       # 공집합과 set_idx와의 합집합
#     set_chk.discard((f_r, f_c))

#     for i in range(4):
#         nr = dr[i] + f_r
#         nc = dc[i] + f_c
#         while 0 <= nr < n and 0 <= nc < n:
#             set_move.add((nr, nc))
#             nr = dr[i] + nr
#             nc = dc[i] + nc
#     set_chk = set_chk - set_move
#     while 1:
#         if not set_chk:
#             return cnt
#         r, c = set_chk.pop()
#         cnt += 1

#         for i in range(4):
#             nr = dr[i] + r
#             nc = dc[i] + c
#             while 0 <= nr < n and 0 <= nc < n:
#                 set_move.add((nr, nc))
#                 nr = dr[i] + nr
#                 nc = dc[i] + nc
#         set_chk = set_chk - set_move


# map1 = []
# set_idx = set()

# n = int(input())

# for i in range(n):
#     map1.append(list(map(int, input().split())))
#     for j, e in enumerate(map1[i]):
#         if e == 1:
#             set_idx.add((i,j))
# set_cycle = list(set_idx)

# sol = []

# for fix_r, fix_c in set_cycle:
#     sol.append(bfs(fix_r, fix_c))

# print(max(sol))