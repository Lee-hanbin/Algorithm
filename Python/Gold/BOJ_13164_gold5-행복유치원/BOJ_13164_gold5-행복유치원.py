# BOJ_13164_gold5-행복유치원

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int,input().split())

lst = list(map(int, input().split()))

hight_gap = [0] * (n-1)

for i in range(n-1):
    hight_gap[i] = lst[i+1] - lst[i] 

hight_gap.sort(reverse=True)

print(sum(hight_gap[k-1:]))