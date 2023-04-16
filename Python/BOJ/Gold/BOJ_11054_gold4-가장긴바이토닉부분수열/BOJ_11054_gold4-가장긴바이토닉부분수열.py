# BOJ_11054_gold4-가장긴바이토닉부분수열

import sys

input = sys.stdin.readline

n = int(input())

sequence = list(map(int, input().split()))

dp = [[0] * n for _ in range(3)]

for i in range(n):
    for j in range(i):
        if sequence[i] > sequence[j] and dp[0][i] < dp[0][j]:
            dp[0][i] = dp[0][j]
    dp[0][i] += 1

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if sequence[i] > sequence[j] and dp[1][i] < dp[1][j]:
            dp[1][i] = dp[1][j]
    dp[1][i] += 1

for i in range(n):
    dp[2][i] = dp[0][i] + dp[1][i] - 1


print(max(dp[2]))