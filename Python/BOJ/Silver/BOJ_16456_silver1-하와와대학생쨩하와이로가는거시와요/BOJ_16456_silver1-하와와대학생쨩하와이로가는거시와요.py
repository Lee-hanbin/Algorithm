# BOJ_16456_silver1-하와와대학생쨩하와이로가는거시와요

import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n+2)

dp[0], dp[1], dp[2] = 1, 1, 2

for i in range(3, n):
    dp[i] = (dp[i-1] + dp[i-3]) % 1000000009

print(dp[-3])