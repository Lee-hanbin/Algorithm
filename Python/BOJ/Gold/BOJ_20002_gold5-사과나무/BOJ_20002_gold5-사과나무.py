# BOJ_20002_gold5-사과나무

import sys

input = sys.stdin.readline

n = int(input())

apple_tree = [list(map(int, input().split())) for _ in range(n)]
cul_map = [[0] * (n+1) for _ in range(n+1)]

sol = -1000
for i in range(n):
    sol = max(sol, max(apple_tree[i]))
    for j in range(n):
        cul_map[i+1][j+1] = apple_tree[i][j] + cul_map[i+1][j] + cul_map[i][j+1] - cul_map[i][j]
# print(sol)
# for i in cul_map:
#     print(*i)
for k in range(1,n):
    for r in range(1, n-k+1):
        for c in range(1, n-k+1):
            # print('r, c :', r, c )
            # print('r+k : ', r+k)
            # print('c+k : ', c+k)
            # print('r-1 : ', r-1)
            # print('c-1 : ', c-1)
            chk = cul_map[r+k][c+k] - cul_map[r+k][c-1] - cul_map[r-1][c+k] + cul_map[r-1][c-1]
            if sol < chk:
                sol = chk
print(sol)


# 1. 무지성 풀이

# import sys

# input = sys.stdin.readline

# n = int(input())

# apple_tree = [list(map(int, input().split())) for _ in range(n)]

# sol = -1000
# for k in range(1, n+1):
    
#     for r in range(n-k+1):
#         for c in range(n-k+1):
#             chk = 0
#             for i in range(k):
#                 chk += sum(apple_tree[r+i][c:c+k])
#             sol = max(sol, chk)

# print(sol)
