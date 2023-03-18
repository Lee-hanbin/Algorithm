# SWEA_1767-프로세서연결하기

import sys

sys.stdin = open('sample_input.txt')

import heapq

#    우  좌 하 상
dr = [0, 0, 1,-1]
dc = [1,-1, 0, 0]

def dfs(idx, cnt, tmp):
    global sol
    
    if idx == length:
        return

    r, c = idx_lst[idx]

    dfs(idx+1, cnt, tmp)    # 현재 코어를 건너뛰는 경우
    
    # 델타 탐색
    for i in range(4):
        nr = dr[i] + r
        nc = dc[i] + c
        chk = tmp

        # 전선 연결 가능여부 파악
        while 0 <= nr < N and 0 <= nc < N and not map1[nr][nc]:
            chk += 1
            nr += dr[i]
            nc += dc[i]

        # 전선 연결 가능한 경우
        if nr == N or nc == N or nr == -1 or nc == -1:

            # 코어의 개수를 최대로
            heapq.heappush(lst, (cnt, chk))
            if i == 0: #우
                map1[r][c+1:N] = [2] * (N-c-1)
                dfs(idx +1, cnt-1, chk)
                map1[r][c+1:N] = [0] * (N-c-1)
            elif i == 1: #좌
                map1[r][0:c] = [2] * (c)
                dfs(idx +1, cnt-1, chk)
                map1[r][0:c] = [0] * (c)
            elif i == 2: #하
                for i in range(r+1, N):
                    map1[i][c] = 2
                dfs(idx +1, cnt-1, chk)
                for i in range(r+1, N):
                    map1[i][c] = 0
            else: # 상
                for i in range(0, r):
                    map1[i][c] = 2
                dfs(idx +1, cnt-1, chk)
                for i in range(0, r):
                    map1[i][c] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    sol = N ** 2
    map1 = []
    idx_lst = []

    # 코어가 가장자리에 있지 않은 것들 체크
    for i in range(N):
        map1.append(list(map(int, input().split())))
        for j, e in enumerate(map1[i]):
            if e:
                if i == 0 or i == N-1 or j == N-1 or j == 0:
                    continue
                idx_lst.append((i,j))
    lst =[]
    length = len(idx_lst)

    dfs(0, length-1, 0)

    print(f'#{t} {heapq.heappop(lst)[1]}')