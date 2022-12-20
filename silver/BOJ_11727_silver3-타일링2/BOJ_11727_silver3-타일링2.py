# BOJ_11727_silver3-타일링2

from math import comb

n = int(input())

# dp 풀이
if n <3:
    dp = [0, 1, 3]
else:
    dp = [0] * (n+1)
    dp[1:3] = [1, 3]
    for i in range(3, n+1):
        dp[i] = dp[i-1] + 2 * dp[i-2]

print(dp[n]%10007)


# 수학적 풀이
# sol = 0
# for i in range(n//2+1):
#     sol += 2**i * comb(n-i,i)
# print(sol%10007)