# BOJ_11052_silver1-카드구매하기

import sys

input = sys.stdin.readline

n = int(input())

price_lst = [0] + list(map(int, input().split()))

# dp = price_lst[::]

# dp[1] = price_lst[1]

for i in range(2,n+1):
    # tmp = price_lst[i]
    price_lst[i] = max(price_lst[j] + price_lst[i-j] for j in range(i//2+1))
    # for j in range(1, i//2 + 1):
    #     price_lst[i] = max(price_lst[i], price_lst[j]+price_lst[i-j])
    # dp[i] = tmp

print(price_lst[-1])