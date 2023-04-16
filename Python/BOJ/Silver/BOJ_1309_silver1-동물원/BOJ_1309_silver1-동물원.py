# BOJ_1309_silver1-동물원

import sys

input = sys.stdin.readline


# 1. backtracking
# sys.setrecursionlimit(1000000)

# def dfs(r, c):
#     global cnt

#     if r == n+2:
#         return
#     cnt += 1

#     for rr in range(r, n+1):
#         for cc in range(2):
#             if rr == r and c == 1 and cc == 0:
#                 continue
#             if not cc: 
#                 if not zoo[rr-1][0]:
#                     zoo[rr][cc] = 1
#                     dfs(rr, 1)
#                     zoo[rr][cc] = 0
#             else:
#                 if not zoo[rr-1][1] and not zoo[rr][0]:
#                     zoo[rr][cc] = 1
#                     dfs(rr+1, 0)
#                     zoo[rr][cc] = 0

# n = int(input())

# zoo = [[0] * 2 for _ in range(n+1)]
# cnt = 0

# dfs(1,0)

# print(cnt)

# 2. dp 2차원 배열
# n = int(input())

# dp = [[0] * 3 for _ in range(n+1)]

# dp[1] = [1, 1, 1]

# for i in range(2, n+1):
#     dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2])%9901
#     dp[i][1] = (dp[i-1][0] + dp[i-1][2])%9901
#     dp[i][2] = (dp[i-1][0] + dp[i-1][1])%9901

# print(sum(dp[n])%9901)    

#3. dp 1차원 배열
n = int(input())

dp = [0] * (n+1)

dp[:2] = [1, 3]

for i in range(2, n+1):
    # 직전 우리에 사자가 없는 경우 + 우리에 사자가 있는 경우 (좌, 우)
    dp[i] = (dp[i-2] + dp[i-1]*2)%9901

print(dp[-1])