# BOJ_14500_gold4-테트로미노

import sys 
from collections import deque

input = sys.stdin.readline

dr = [-1, 0 ,0, 1]
dc = [ 0,-1, 1, 0]


# 연속해서 갈 수 있는 경우 체크
def bfs(idx):
    que =deque()
    visited = set()
    i, j = idx
    visited.add((i,j))
    sol = 0
    que.append(( i, j , 1, map1[i][j], visited))
    while que:
        r, c, cnt, tmp, cul_idx = que.popleft()
        if cnt == 4:
            sol = max(sol, tmp)
        for i in range(3):              # 아래, 왼쪽, 오른쪽만 체크하면 된다.
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nr < Row and 0 <= nc < Col and cnt < 4 and (nr, nc) not in cul_idx:
                next_idx = cul_idx|{(nr, nc)}
                que.append((nr,nc, cnt + 1, tmp + map1[nr][nc], next_idx))
    return sol                

# ㅗ, ㅓ, ㅜ, ㅏ 처리
def exception_case(idx):
    r, c = idx
    if idx == (0,0) or idx == (Row-1, Col-1) or idx == (0, Col - 1) or idx == (Row - 1, 0): 
        return 0
    elif r == 0:    #위쪽 벽
        return map1[0][c-1] + map1[0][c] + map1[0][c+1] + map1[1][c]
    elif c == 0:    #왼쪽 벽
        return map1[r-1][0] + map1[r][0] + map1[r+1][0] + map1[r][1]
    elif r == Row -1:   # 아래쪽 벽
        return map1[r][c-1] + map1[r][c] + map1[r][c+1] + map1[r-1][c]
    elif c == Col -1:   # 오른쪽 벽
        return map1[r-1][c] + map1[r][c] + map1[r+1][c] + map1[r][c-1]
    else:           # 벽x
        sol = 0
        base = map1[r][c] + map1[r-1][c] + map1[r][c+1] + map1[r+1][c] + map1[r][c-1]   # 자신 포함 네 방향 모두 더하기
        for i in range(4):          # delta search를 통해서 한 방향씩 빼고 가장 큰 값 반환
            nr = dr[i] + r
            nc = dc[i] + c
            sol = max(sol, base - map1[nr][nc])
        return sol

Row, Col = map(int, input().split())

map1 = [list(map(int, input().split())) for _ in range(Row)]

rst = 0
for i in range(Row):
    for j in range(Col):
        tmp = max(bfs((i,j)), exception_case((i,j)))
        rst = max(rst, tmp)

print(rst)