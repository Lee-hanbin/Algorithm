# BOJ_10830_gold4-행렬제곱

import sys

input = sys.stdin.readline


def power(matrix, k):
    if k == 1:
        return matrix
    chk = power(matrix, k//2)
    tmp = matrix_multi(chk, chk)

    if not k % 2:
        return tmp
    else:
        return matrix_multi(matrix, tmp)

def matrix_multi(A, B):
    BT = []
    for i in zip(*B):
        BT.append(list(i))

    sol = A[::]
    for i in range(N):
        tmp = []
        for j in range(N):
            chk = 0
            for e in range(N):
                chk += sol[i][e] * BT[j][e]
            tmp.append(chk%1000)
        sol[i] = tmp
    return sol

N, B = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        A[i][j] %= 1000
        
res = power(A, B)

for i in res:
    print(*i)


#2. 무지성 행렬곱
# N, B = map(int, input().split())

# A = [list(map(int, input().split())) for _ in range(N)]
# AT = []
# for i in zip(*A):
#     AT.append(list(i))

# sol = A[::]
# dp = []
# dp.append(A)

# k = 1
# while k < B:
#     k += 1
#     for i in range(N):
#         tmp = []
#         for j in range(N):
#             chk = 0
#             for e in range(N):
#                 chk += sol[i][e] * AT[j][e]
#             tmp.append(chk%1000)
#         sol[i] = tmp
#     if A == sol:
#         break
#     dp.append(sol)
# if k == B:
#     for i in dp[-1]:
#         print(*i)
# else:
#     for i in dp[B%k]:
#         print(*i)