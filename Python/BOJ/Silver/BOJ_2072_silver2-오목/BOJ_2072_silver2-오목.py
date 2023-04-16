# BOJ_2072_silver2-오목

import sys
input = sys.stdin.readline

dr = [ 1, 0, 1,-1]
dc = [ 0, 1, 1, 1]

# dfs 서치
def dfs(r, c, map1):
    ckh_num = n + 1
    for i in range(4):
        nr = dr[i] + r
        nc = dc[i] + c

        cnt = 1
        lst = [map1[r][c]]
        
        # 처음 두는데 이미 뒀던 돌이면 pass
        if len(lst) == 1:
            if 0 <= r-dr[i] < 19 and 0 <= c-dc[i] < 19 and map1[r-dr[i]][c-dc[i]] > 0:
                continue
        
        # 두고 있는 방향 체크하여 연속되는 돌이 몇 개 인지 체크
        while 0 <= nr < 19 and 0 <= nc < 19 and map1[nr][nc] > 0:
            cnt += 1
            lst.append(map1[nr][nc])
            nr = dr[i] + nr
            nc = dc[i] + nc
        
        # 오목이면 값 갱신
        if len(lst) == 5:
            chk = max(lst)
            ckh_num = min(chk, ckh_num)

    return ckh_num

n = int(input())

black_map = [[0]* 19 for _ in range(19)]
white_map = [[0]* 19 for _ in range(19)]

# 흑돌과 백돌 오목판에 각각 두기
for i in range(1, n+1):
    r, c = map(int, input().split())
    if i % 2:
        black_map[r-1][c-1] = i
    else:
        white_map[r-1][c-1] = i

sol = n + 1

# 오목판 순회
for i in range(19):
    for j in range(19):
        # 흑돌 탐색
        if black_map[i][j] > 0:
            tmp = dfs(i, j, black_map)
            sol = min(sol, tmp)
        # 백돌 탐색
        if white_map[i][j] > 0:
            tmp = dfs(i, j, white_map)
            sol = min(sol, tmp)

if sol == n + 1:
    print(-1)
else:
    print(sol)