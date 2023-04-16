# BOJ_2531_silver1-회전초밥

import sys
from collections import deque

input = sys.stdin.readline

n, d, k, c = map(int, input().split())

lst = list(int(input()) for _ in range(n))

sol = 0
for i in range(n):
    chk_set = set(lst[i:i+k] + [c])
    if i+k > n:
        chk_set = chk_set | set(lst[:i+k-n])
    tmp = len(chk_set)
    sol = max(sol, tmp)
print(sol)
    
# que = deque(int(input()) for _ in range(n))

# sol = 0
# for _ in range(n):
#     chk_lst = list(que)
#     chk_set = set(chk_lst[:k]) 
#     chk_set.add(c)
#     tmp = len(chk_set)
#     sol = max(sol, tmp)
#     que.rotate(-1)
#     # print(que)
# print(sol)