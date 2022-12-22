# BOJ_18353_silver2-병사배치하기

n = int(input())
power = list(map(int, input().split()))

dp = [0] * n
dp[0] = (1, power[0])

for i in range(1,n):
    if power[i-1] > power[i]:
        dp[i][0] = dp[i][0] + 1