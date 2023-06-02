# BOJ_14003_platinum5-가장긴증가하는부분수열5

import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

seq = [lst[0]]
tmp = []

for num in lst:
    if seq[-1] < num:
        seq.append(num)
        tmp.append((len(seq)-1, num))
    else:
        idx = bisect_left(seq, num)
        seq[idx] = num
        tmp.append((idx, num))

last_idx = len(seq) - 1
sol = []

for i in range(n-1, -1, -1):
    if tmp[i][0] == last_idx:
        sol.append(tmp[i][1])
        last_idx -= 1         

print(len(seq))
print(*sol[::-1])