# BOJ_17281_gold4-야구

import sys
from itertools import permutations

input = sys.stdin.readline


# 야구 시작
def play(hitter_lst, hitter):
    score = 0
    # 이닝 만큼 진행
    for inning in range(n):
        out= 0
        tag1, tag2, tag3 = 0, 0, 0
        # 3아웃될때까지 이닝 진행
        while out < 3:
            # if out == 3:
            #     out = 0
            #     break

            # 순서
            hitter = hitter % 9
            # 순서에 해당하는 타자의 타격결과
            status = innings[inning][hitter_lst[hitter]]

            if not status:
                out += 1
            elif status == 1:
                score += tag3
                tag1, tag2, tag3 = 1, tag1, tag2
            elif status == 2:
                score += tag2 + tag3
                tag1, tag2, tag3 = 0, 1, tag1                
            elif status == 3:
                score += tag1 + tag2 + tag3
                tag1, tag2, tag3 = 0, 0, 1
            else:
                score += 1 + tag1 + tag2 + tag3
                tag1, tag2, tag3 = 0, 0, 0                

            hitter += 1
    return score

n = int(input())

innings = [list(map(int, input().split())) for _ in range(n)]
tmp = []

sol = 0

# 첫 타자가 1번타자부터 9번타자까지 4번 타자는 항상 첫 타자
for start in permutations([1,2,3,4,5,6,7,8], 8):
    tmp = list(start)[:3] + [0] + list(start)[3:]
    sol = max(sol, play(tmp, 0))
print(sol)