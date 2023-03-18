# BOJ_1766_gold2-문제집

import sys
from collections import defaultdict
from heapq import heappush, heappop

input = sys.stdin.readline

n, m = map(int, input().split())

lst = [0] * (n+1)
dict1 = defaultdict(list)

for _ in range(m):
    A, B = map(int, input().split())
    lst[B] += 1
    dict1[A].append(B)

que = []
for i in range(1, n+1):
    if not lst[i]:
        heappush(que, i)

sol = []
while que:
    i = heappop(que)
    sol.append(i)

    if i in dict1:
        for j in dict1[i]:
            lst[j] -= 1
            if not lst[j]:
                heappush(que, j)

print(*sol)

# 1. 무지성
# cnt = n

# while chk_set:
#     for idx, num in enumerate(lst):
#         if not num and idx not in chk_set:
#             sol.append(idx)
#             lst[idx] = 1
#             chk_set.discard(chk_lst[idx])
#             cnt -= 1
#             break

# for i, num in enumerate(lst):
#     if not num:
#         sol.append(i)

# print(*sol[1:])

