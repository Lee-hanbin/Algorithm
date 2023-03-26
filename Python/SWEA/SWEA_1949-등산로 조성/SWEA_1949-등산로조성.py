# SWEA_1949-등산로 조성

import sys
sys.stdin = open("sample_input.txt")

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

def dfs(r, c, cnt):
    global sol, switch
    sol = max(cnt, sol)

    for i in range(4):
        nr = dr[i] + r
        nc = dc[i] + c
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:

            # 다음 길이 현재 길보다 낮으면 바로 길 뚫기
            if map1[nr][nc] < map1[r][c]:
                visited[nr][nc] = 1
                dfs(nr, nc, cnt + 1)
                visited[nr][nc] = 0
            # 다음 길이 현재 길보다 높거나 같은 경우,
            else:
                # 아직 높이 조정을 안했으면
                if not switch:
                    # 높이 조정 시, 주어진 높이보다 작거나 같은 경우, 조정하고 switch on 
                    tmp = map1[nr][nc] - map1[r][c] + 1
                    if tmp <= k:
                        map1[nr][nc] -= tmp
                        visited[nr][nc] = 1
                        switch = 1
                        dfs(nr, nc, cnt + 1)
                        switch = 0
                        visited[nr][nc] = 0
                        map1[nr][nc] += tmp




T = int(input())

for t in range(1, T+1):
    n, k = map(int, input().split())
    
    map1 = list(list(map(int, input().split())) for _ in range(n))
    
    visited = list([0] * n for _ in range(n))
    max_h = 0
    
    # 가장 높은 봉우리 크기 찾기
    for i in map1:
        max_h = max(max_h, max(i))
    
    sol = 0

    # 가장 높은 봉우리 찾아서 등산로 조성
    for i in range(n):
        for j in range(n):
            if map1[i][j] == max_h:
                switch = 0
                visited[i][j] = 1
                dfs(i, j, 1)
                visited[i][j] = 0
    

    print(f'#{t} {sol}')

                

    