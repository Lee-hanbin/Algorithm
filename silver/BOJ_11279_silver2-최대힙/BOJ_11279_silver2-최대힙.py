# BOJ_11279_silver2-최대힙

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())
lst = []
lst_zero = [1] * n
cnt = 0
for i in range(n):
    num = int(input()) * -1
    if len(lst) == 0:
        if num == 0:
            print(0)
        else:
            heappush(lst, num)
    else:
        if num == 0:
            sol = -1 * heappop(lst)
            print(sol)
        else:
            heappush(lst, num)
        

