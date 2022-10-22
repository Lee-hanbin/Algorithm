# BOJ_2579_silver3-계단오르기

n = int(input())

lst = [0]
dp = [0] * (n+1)
for i in range(n):
    lst.append(int(input().strip()))

dp[1] = lst[1]
if n== 1:
    print(dp[1])
    exit()
dp[2] = lst[2] + lst[1]

for i in range(3, n+1):
    dp[i] = max(dp[i-2]+lst[i], dp[i-3]+lst[i-1]+lst[i])
print(dp[n])