# BOJ_1562_gold1-계단수

MOD = 1000000000

n = int(input())

# 1<<10 = 2^10
dp = [[list(0 for _ in range(1<<10)) for _ in range(10)] for _ in range(n+1)]

# print(1<<10)

for i in range(10):
    dp[1][i][1<<i] = 1

for i in range(2, n+1):
    for j in range(10):
        for k in range(1 << 10):
            if not j:
                dp[i][j][(1<<j)|k] += dp[i-1][j+1][k]
            elif j == 9:
                dp[i][j][(1<<j)|k] += dp[i-1][j-1][k]
            else:
                dp[i][j][(1<<j)|k] += dp[i-1][j-1][k]
                dp[i][j][(1<<j)|k] += dp[i-1][j+1][k]
            
            dp[i][j][(1<<j)|k] %= MOD

sol =  0
for i in range(1, 10):
    sol += dp[n][i][(1<<10)-1]
    sol %= MOD

print(sol)