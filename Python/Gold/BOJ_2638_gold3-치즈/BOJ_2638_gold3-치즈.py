# BOJ_2638_gold3-치즈

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

board = []

cheeze = 0
for i in range(n):
    board.append(list(map(int, input().split())))

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

sol = 0

start = {(0, 0), (0, m-1), (n-1, 0), (n-1, m-1)}

for r, c in start:
    board[r][c] = 2

while 1:
    melt_lst = []
    while start:
        check_set = set()
        for r, c in start:
            for i in range(4):
                nr = dr[i] + r
                nc = dc[i] + c
                if 0 <= nr < n and 0 <= nc < m:
                    if not board[nr][nc]:
                        check_set.add((nr, nc))
                        board[nr][nc] = 2
                    if board[nr][nc] == 1:
                        melt_lst.append((nr, nc))       
        start = check_set
    
    if not melt_lst:
        print(sol)
        break
    sol += 1

    start = set()
    for r, c in melt_lst:
        cnt = 0
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 2:
                cnt += 1
                if cnt == 2:
                    start.add((r, c))
                    break

    for x, y in start:
        board[x][y] = 2