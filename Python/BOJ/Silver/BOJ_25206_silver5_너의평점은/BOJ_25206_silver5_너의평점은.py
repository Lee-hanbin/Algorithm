# BOJ_25206_silver5_너의평점은

import sys
input = sys.stdin.readline

# 전공평점 = sum(학점 * 과목평점) / sum(학점)
# P는 계산제외

sol = 0
cnt = 0

chk = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0,
}



for _ in range(20):
    name, score, rank = input().split()
    if rank == 'P':
        continue
    score = float(score)
    cnt += score
    sol += score * chk[rank]

print(sol/cnt)