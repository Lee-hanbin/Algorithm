# BOJ_17070_gold5-파이프옮기기1


import sys
from collections import deque

input = sys.stdin.readline

#1. bfs(완탐) 시간초과

# # type 1: 가로
# # type 2: 대각
# # type 3: 세로

# def bfs():
#     que = deque()
#     que.append((1, 0, 1))
#     cnt = 0
#     while que:
#         pipetype, r, c = que.popleft()
#         if r == n-1 and c == n-1:
#             cnt += 1
#         if pipetype == 1 and c < n - 1 and not map1[r][c+1]:
#             que.append((1, r, c+1))
#             if r < n - 1 and not map1[r+1][c+1] and not map1[r+1][c]:
#                 que.append((2, r+1, c+1))
#         elif pipetype == 2:
#             if c < n - 1 and not map1[r][c+1]:
#                 que.append((1, r, c+1))
#                 if r < n - 1 and not map1[r+1][c+1] and not map1[r+1][c]:
#                     que.append((2, r+1, c+1))
#             if r < n - 1 and not map1[r+1][c]:
#                 que.append((3, r+1, c))
#         elif pipetype == 3 and r < n - 1 and not map1[r+1][c]:
#             que.append((3, r+1, c))
#             if c < n - 1 and not map1[r+1][c+1] and not map1[r][c+1]:
#                 que.append((2, r+1, c+1))
#     return cnt

# n = int(input())

# map1 = [list(map(int, input().split())) for _ in range(n)]

# if map1[n-1][n-1] or (map1[n-1][n-2] and map1[n-2][n-1]):
#     print(0)
# else:
#     print(bfs())


#2. dp

n = int(input())

map1 = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0] * n for _ in range(n)] for _ in range(3)]

# 첫 파이프는 가로
dp[0][0][1] = 1

# 첫 파이프가 가로 이므로 첫 col 초기화
for i in range(2, n):
    if not map1[0][i]:
        dp[0][0][i] = dp[0][0][i-1]


for r in range(1, n):
    for c in range(1, n):
        # 대각선
        if not map1[r][c] and not map1[r][c-1] and not map1[r-1][c]:
            dp[2][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]
        
        if not map1[r][c]:
            # 가로
            dp[0][r][c] = dp[0][r][c-1] + dp[2][r][c-1]
            # 세로
            dp[1][r][c] = dp[1][r-1][c] + dp[2][r-1][c]

print(sum(dp[i][n-1][n-1] for i in range(3)))