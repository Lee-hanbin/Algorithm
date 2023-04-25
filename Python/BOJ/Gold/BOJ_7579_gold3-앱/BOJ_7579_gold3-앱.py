# BOJ_7579_gold3-앱

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memories = list(map(int, input().split()))
cost = list(map(int, input().split()))

sol = 100*100
max_cost = sum(cost) + 1
dp = [[0] * max_cost for _ in range(n+1)]

if not m:
    print(0)
else:
    for i in range(1, n+1):
        byte = memories[i-1]
        c = cost[i-1]

        for j in range(1, max_cost):
            if j < c:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(byte + dp[i-1][j-c], dp[i-1][j])
            
            if dp[i][j] >= m:
                sol = min(sol, j)

    print(sol)