# BOJ_2467_gold5-용액

import sys

input = sys.stdin.readline

INF = float('inf')

n = int(input())
lst = list(map(int, input().split()))

# 0보다 큰 값이 나타나면 슬라이싱
for i, e in enumerate(lst):
    if e > 0:
        acid_lst = lst[i:]
        alcalic_lst = lst[:i][::-1]
        break
# 모두 음수이면 가장 큰 음수 두 개 출력
else:
    print(lst[-2], lst[-1])
    exit()

# 세 경우 초기화
case_1 = [INF, INF, INF]
case_2 = [INF, INF, INF]
case_3 = [INF, INF, INF]

# 1. 양수가 두 개 이상인 경우만
if len(acid_lst) > 1:
    case_1 = [acid_lst[0] + acid_lst[1], acid_lst[0], acid_lst[1]]

# 2. 음수가 두 개 이상인 경우만
if len(alcalic_lst) > 1:
    case_2 = [alcalic_lst[1] + alcalic_lst[0], alcalic_lst[1], alcalic_lst[0]]

# 3. 양수와 음수 모두 존재하는 경우만
if acid_lst and alcalic_lst and case_3[0] != 0:
    # 0에 근접한 수 뽑기
    i, j = 0, 0
    while i < len(acid_lst) and j < len(alcalic_lst):
        chk = acid_lst[i] + alcalic_lst[j]
        if abs(chk) < case_3[0]:
            case_3 = abs(chk), alcalic_lst[j], acid_lst[i]
        if chk < 0:
            i += 1
        else:
            j += 1
    
# 세 경우 중에 가장 작은 값
sol = min(case_1[0], abs(case_2[0]), case_3[0])

# 해당하는 값 출력
if sol == case_1[0]:
    print(*case_1[1:])
elif sol == abs(case_2[0]):
    print(*case_2[1:])
else:
    print(*case_3[1:])