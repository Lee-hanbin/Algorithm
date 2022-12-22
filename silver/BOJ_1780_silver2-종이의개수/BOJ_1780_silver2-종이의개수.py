# BOJ_1780_silver2-종이의개수

import sys

input = sys.stdin.readline


def chk(r, c, n):
    global sol_m1, sol_0, sol_1
    # 맵의 요소가 하나인 경우, 값을 더하고 재귀에서 탈출한다.
    if n == 1:
        sol = map1[r][c]
        if sol == -1:
            sol_m1 += 1
        elif sol == 0:
            sol_0 += 1
        else:
            sol_1 += 1
        return 
    # 맵의 크기가 3이상인 경우,
    sol = 0
    # 모든 요소의 합을 구한다
    for i in range(r, r+n):
        sol += sum(map1[i][c:c+n])
        
    if sol == n**2:     # 합의 크기가 맵의 크기와 같고 양수이면 1
        sol_1 += 1
    elif sol == -n**2:  # 합의 크기가 맵의 크기와 같고 음수이면 1
        sol_m1 += 1
    elif sol == 0:      # 합의 크기가 0이면

        # 모든 요소가 0인지 판별하는 함수
        def chk2(r, c, n):
            for i in range(r, r+n):
                for j in range(c, c+n):
                    if map1[i][j]:
                        return True
            else:
                return False

        if chk2(r, c, n):                           # 하나라도 요소가 0이 아니면 9조각 쪼개기
            for i in range(r, r+n, n//3):
                for j in range(c, c+n, n//3):
                    chk(i, j, n//3)
        else:                                       # 모든 요소가 0인 경우
            sol_0 += 1
    else:                                           # 어떠한 경우에도 속하지 않으면 9조각 쪼개기
        for i in range(r, r+n, n//3):
            for j in range(c, c+n, n//3):
                chk(i, j, n//3)

n = int(input())
sol_m1 = 0
sol_0= 0
sol_1 = 0

map1 = [list(map(int, input().split())) for _ in range(n)]

chk(0,0,n)
print(sol_m1)
print(sol_0)
print(sol_1)