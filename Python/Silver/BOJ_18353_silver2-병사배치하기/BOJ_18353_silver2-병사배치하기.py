# BOJ_18353_silver2-병사배치하기

n = int(input())
power = list(map(int, input().split()))

dp = [1] * n

# for i in range(1, n):
#     for j in range(0, i):
#         if power[j] > power[i]:
#             dp[i] = max(dp[i], dp[j] + 1)

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if power[j] < power[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
