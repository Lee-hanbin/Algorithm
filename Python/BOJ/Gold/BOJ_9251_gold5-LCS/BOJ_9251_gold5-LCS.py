# BOJ_9251_gold5-LCS

import sys

input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

n = len(s1)
m = len(s2)

dp = [[0] * (n + 1) for _ in range(m+1)]

for j in range(1, n+1):
    for i in range(1, m+1):
        if s1[j-1] == s2[i-1]:              # 문자가 같으면 좌상단 + 1
            dp[i][j] = dp[i-1][j-1] + 1
        else:                               # 문자가 다르면 max( 좌측, 우측)
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])


for i in dp:
    print(*i)
