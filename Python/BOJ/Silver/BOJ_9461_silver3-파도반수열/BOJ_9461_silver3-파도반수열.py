# BOJ_9461_silver3-파도반수열

import sys
input = sys.stdin.readline

T = int(input())

lst=[0]*T
for i in range(T):
    lst[i]=int(input().strip())

chk = max(lst)
if chk > 5:
    dp=[0]*(chk+1)
    dp[1]=1
    dp[2]=1
    dp[3]=1
    dp[4]=2
    dp[5]=2
    for i in range(6,chk+1):
        dp[i]=dp[i-1] + dp[i-5]
else:
    dp = [0,1,1,1,2,2]
    
for i in lst:
    print(dp[i])