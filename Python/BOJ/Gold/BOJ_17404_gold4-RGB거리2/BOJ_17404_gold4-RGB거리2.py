# BOJ_17404_gold4-RGB거리2

import sys

input = sys.stdin.readline

n = int(input())

dp = [[[0, 0, 0] for _ in range(n-1)] for _ in range(3)]

#1. 첫번째 => r, n번째 g or b
#  첫번째 => g, n번째 r or b
#  첫번째 => b, n번째 r or g
r, g, b = map(int, input().split())
dp[0][0] = r, g, b
dp[1][0] = r, g, b
dp[2][0] = r, g, b

#2. 두번째 => 첫번째와 다른 색으로 칠하기
r, g, b = map(int, input().split())
dp[0][1] = 2000, dp[0][0][0] + g, dp[0][0][0] + b
dp[1][1] = dp[0][0][1] + r, 2000, dp[0][0][1] + b
dp[2][1] = dp[0][0][2] + r, dp[0][0][2] + g, 2000

#3. 세번쩨 ~ n-1번째
for i in range(2, n-1):
    r, g, b = map(int, input().split())
    for j in range(3):
        dp[j][i][0] = min(dp[j][i-1][1], dp[j][i-1][2]) + r
        dp[j][i][1] = min(dp[j][i-1][0], dp[j][i-1][2]) + g
        dp[j][i][2] = min(dp[j][i-1][0], dp[j][i-1][1]) + b

#4. n번째 => 첫번째와 n-1번째와 무관한 값 찾기
r, g, b = map(int, input().split())
red = min(dp[0][-1][0]+min(g, b), dp[0][-1][1] + b, dp[0][-1][2] + g)
green = min(dp[1][-1][0] + b, dp[1][-1][1] + min(r, b) ,dp[1][-1][2] + r)
blue = min(dp[2][-1][0] + g, dp[2][-1][1] + r, dp[2][-1][2] + min(r, g))
print(min(red, green, blue))