# BOJ_2636_gold4-치즈

import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

def bfs():
    que = deque()
    que.append((0,0))
    visited = {(0,0)}
    melting_lst = []
    while que:
        r,c = que.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
                if board[nr][nc]:
                    melting_lst.append((nr,nc))
                else:
                    que.append((nr,nc))
                visited.add((nr, nc)) 
    # 치즈를 다 녹여
    for r,c in melting_lst:     
        board[r][c] = 0
    return len(melting_lst)

n, m = map(int, input().split())


sol = 0
board = []
before_cnt = 0
initial_cheeze = 0


for i in range(n):
    board.append(list(map(int, input().split())))
    for j in board[i]:
        if j == 1:
            initial_cheeze += 1

# 모든 치즈가 녹을 때까지 실행
while initial_cheeze:
    sol += 1            
    before_cnt = bfs()  # before_cnt는 이전 bfs에서 녹인 치즈의 수
    initial_cheeze -= before_cnt

print(sol)
print(before_cnt)