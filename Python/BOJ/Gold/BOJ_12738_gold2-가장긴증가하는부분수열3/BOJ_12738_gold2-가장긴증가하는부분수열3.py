# BOJ_12738_gold2-가장긴증가하는부분수열3

import sys
from bisect import bisect_left

n = int(input())
lst = list(map(int, input().split()))
seq = [lst[0]]
ans = 1

for num in lst[1:]:
    if seq[-1] < num:
        seq.append(num)
        ans += 1
    else:
        index = bisect_left(seq, num)
        seq[index] = num

print(ans)