# SWEA_6190_d3-정곤이의단조증가하는수

import sys

sys.stdin =open("s_input.txt")

# 단조증가 판별 함수
def isMono(num):
    # 끝값이 0이면 -1 return
    if not num[-1]:
        return -1
    # 단조증가 판별
    for i in range(1, len(num)):
        if num[i-1] > num[i]:
            return -1
    else:
        return int(num)
    

T = int(input())

for t in range(1,T+1):
    n = int(input())
    number_set = list(map(int, input().split()))
    sol = -1
    for i in range(n):
        for j in range(i+1,n):
            sol = max(sol, isMono(str(number_set[i] * number_set[j])))
    print(f'#{t} {sol}')