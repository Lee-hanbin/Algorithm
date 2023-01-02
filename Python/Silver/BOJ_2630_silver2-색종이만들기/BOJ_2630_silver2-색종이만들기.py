# BOJ_2630_silver2-색종이만들기

import sys
input = sys.stdin.readline

def rec_f(idx, n):
    global sol_one, sol_zero

    r, c = idx

    if n == 1:                  # 종이의 크기가 1이면
        if map1[r][c] == 1:     # 파랑이면
            sol_one += 1        # 파랑색 종이 + 1
        else:                   # 하양이면
            sol_zero += 1       # 하얀색 종이 + 1
        return

    chk_sol = 0
    for i in range(r,r+n):                  # 색종이의 요소의 합 구하기
        chk_sol += sum(map1[i][c:c+n])

    if chk_sol == n**2:                     # 요소의 합이 색종이의 크기와 같으면
        sol_one += 1                        # 파랑색 종이 + 1
    elif chk_sol == 0:                      # 요소의 합이 0이면
        sol_zero += 1                       # 하양색 종이 + 1
    else:                                   # 색종이가 섞여 있으면
        for i in [(r,c), (r + n//2, c), (r, c + n//2), (r + n//2, c + n//2)]:       # 4개로 색종이 나누기
            rec_f(i, n//2)


N = int(input())

map1 = [list(map(int, input().split())) for _ in range(N)]

sol_zero = 0
sol_one = 0
chk_sol = 0


rec_f((0,0), N)

print(sol_zero)
print(sol_one)