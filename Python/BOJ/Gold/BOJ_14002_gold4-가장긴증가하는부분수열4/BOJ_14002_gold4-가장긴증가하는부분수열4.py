# BOJ_14002_gold4-가장긴증가하는부분수열4

import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))
seq = [lst[0]]
ans = 1 
sol = []
M = 0

for num in lst[1:]:
    if seq[-1] < num:
        seq.append(num)
        ans += 1
    else:
        index = bisect_left(seq, num)
        seq[index] = num
    if ans > M:
        sol = seq

print(ans)
print(*sol)