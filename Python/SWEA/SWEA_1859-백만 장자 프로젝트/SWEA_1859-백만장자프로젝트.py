# SWEA_1859-백만 장자 프로젝트

import sys

sys.stdin = open("input.txt")

T = int(input().rstrip())

for t in range(1, T+1):
    n = int(input().rstrip())
    
    trade = list(map(int, input().split()))

    dp = [0] * (n + 1 )

    sell_price = 0
    
    for idx in range(n-1, -1, -1):
        market_price = trade[idx]
        if idx == n-1:
            sell_price = market_price
            continue
        if sell_price < market_price:
            dp[idx] = dp[idx + 1]
            sell_price = market_price
        else:
            margin = sell_price - market_price
            dp[idx] = dp[idx + 1] + margin

    print(f'#{t} {dp[0]}')