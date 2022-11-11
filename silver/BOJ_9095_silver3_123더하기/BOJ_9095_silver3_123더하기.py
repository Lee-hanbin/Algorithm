# BOJ_9095_silver3_123더하기

lst=[]
for _ in range(int(input())):
    lst.append(int(input()))
K=max(lst)
dp=[0]*(K+1)
dp[1]=1
if K >1:
	dp[2]=2
if K >2:
	dp[3]=4
for i in range(4,K+1):
	dp[i]=(dp[i-1]+ dp[i-2]+ dp[i-3])
for i in lst:
	print(dp[i])