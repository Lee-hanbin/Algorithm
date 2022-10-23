# BOJ_1463_silver3-1로만들기

n = int(input())
dp = [0] * (int(1e6)+1)
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[n])