# BOJ_9252_gold4-LCS

import sys

input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

n = len(s1)
m = len(s2)

dp = [[''] * (n + 1) for _ in range(m+1)]

for j in range(1, n+1):
    for i in range(1, m+1):
        if s1[j-1] == s2[i-1]:
            dp[i][j] = dp[i-1][j-1] + s1[j-1]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
sol = len(dp[-1][-1])

print(sol)
if sol:
    print(dp[-1][-1])

for i in dp:
    print(*i)