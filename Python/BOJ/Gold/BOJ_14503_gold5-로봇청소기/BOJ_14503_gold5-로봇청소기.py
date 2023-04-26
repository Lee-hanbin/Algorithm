# BOJ_14503_gold5-로봇청소기

import sys

input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [ 0, 1, 0,-1]

n, m = map(int, input().split())

sr, sc, d = map(int, input().split())

map1 = [list(map(int, input().split())) for _ in range(n)]


map1[sr][sc] = 2
sol = 1
flag = 0

while 1:
    for i in range(3, -1, -1):
        tmp_d = (d + i) % 4
        nr = dr[tmp_d] + sr
        nc = dc[tmp_d] + sc
        if not map1[nr][nc]:
            map1[nr][nc] = 2
            sol += 1
            sr, sc, d = nr, nc, tmp_d
            break
    else:
        sr = sr - dr[d]
        sc = sc - dc[d]
        if map1[sr][sc] == 1:
            break
print(sol)


