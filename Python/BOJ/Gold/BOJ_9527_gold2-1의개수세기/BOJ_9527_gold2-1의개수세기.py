# BOJ_9527_gold2-1의개수세기

import sys
from math import log10, log2

input = sys.stdin.readline

a, b = map(int ,input().split())


dp = [0] * int(log2(10**16)+1)

dp[0] = 0
dp[1] = 1
dp[2] = (dp[1] * 2 + 2)
dp[3] = (dp[2] * 2 + 4)
dp[4] = (dp[3] * 2 + 8)
for i in range(5, int(log2(b))+1):
    dp[i] = dp[i-1]*2 + 2**(i-1)

# print(dp)

def operator(num):
    cnt = 0
    bin_num = bin(num)[2:]
    length = len(bin_num)

    for i in range(length):
        if bin_num[i] == '1':
            pow = length - i - 1
            cnt += dp[pow]
            cnt += (num -2**pow + 1)
            num = num - (2**pow)

    return cnt


print(operator(b) - operator(a-1))