# BOJ_12865_gold5-평범한배낭

import sys

input = sys.stdin.readline
n, k = map(int,input().split())

lst = [[0,0]] + [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = lst[i]
    for j in range(1, k+1):
        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[-1][-1])

