# BOJ_11726_silver3_타일링

from math import comb

n = int(input())

# # 수학적 풀이
# sol = 0
# for i in range(n//2+1):
#     sol += comb(n-i, i)

# print(sol % 10007)


# dp 풀이
dp = [0] * (n+1)

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n] % 10007)