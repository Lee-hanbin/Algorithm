# BOJ_11659_silver3_-구간합구하기4

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
cul_lst = [0] * (N + 1)
cul_lst[1] = lst[0]
for i in range(2,N+1):
    cul_lst[i] = cul_lst[i-1] + lst[i-1]

# print(cul_lst)

for i in range(M):
    I, J = map(int, input().split())
    print(cul_lst[J]- cul_lst[I-1])