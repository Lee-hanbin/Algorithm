# BOJ_18310_silver3-안테나

import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(list(map(int, input().split())))

print(lst[(n-1)//2])

# chk = float('inf')
# idx = 0
# for i in range(n):
#     sum1 = 0
#     for j in range(n):
#         sum1 += abs(lst[i] - lst[j])
#         if sum1 > chk:
#             break
#     else:
#         if sum1 < chk:
#             chk = sum1
#             idx = lst[i]
# print(idx)