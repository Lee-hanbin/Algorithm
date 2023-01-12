# BOJ_13908_silver2-비밀번호

import sys
from itertools import product

input = sys.stdin.readline

n, m = map(int, input().split())
if m:
    set_chk = set(map(int, input().split()))
else:
    set_chk = set()

sol = 0
# 중복순열로 10개 중에 n개를 중복이 가능하게 뽑고 선견지명에서 찾을 수 없으면 배제
for i in product(list(range(10)),repeat = n):
    for j in set_chk:
        if j not in i:
            break
    else:
        sol += 1
print(sol)