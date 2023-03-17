# BOJ_17281_gold4-야구

import sys
from collections import deque

input = sys.stdin.readline


def play(hitter):
    score = 0
    cnt = 0
    for inning in range(n):
        out= 0
        while 1:
            if out == 3:
                out = 0
                break

            hitter = hitter % 9
            cnt += innings[inning][hitter]

            if innings[inning][hitter]:
                if cnt // 4:
                    score += (cnt % 4 + 1)
                    cnt = 0
            else:
                out += 1

            print('hitter, score, cnt, out', hitter, score, cnt, out)   
            hitter += 1  

    return score
# 24 + 7 + 8 + 8
n = int(input())

innings = [list(map(int, input().split())) for _ in range(n)]
tmp = [[0] * 9 for _ in range(n)]

sol = 0

# 첫 타자가 1번타자부터 9번타자까지 
for start in range(9):
    chk = (start + 4)
    for i in range(n):
        innings[i] = innings[i][1:4] + innings[i][0] + innings[i][4:]


    sol = max(sol, play(start))

print(sol)