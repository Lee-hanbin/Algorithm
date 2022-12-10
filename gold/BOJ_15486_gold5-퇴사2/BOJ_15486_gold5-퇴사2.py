# BOJ_15486_gold5-퇴사2

import sys
input = sys.stdin.readline

N = int(input().strip())
t_lst = [0] * (N+1)
p_lst = [0] * (N+1)
dp = [0] *(N+2)             
# 만약 상담 일정 + 상담일이 정확히 마지막 날이면 
# t_lst[i]+i > N 이므로 dp를 N+2까지 만들어줘야한다.                      

for i in range(1,N+1):
    t, p = map(int, input().split())
    t_lst[i] = t
    p_lst[i] = p
j = 1
for i in range(N,0,-1):
    if t_lst[i] + i - 1 > N:                            # 해당 예약종료 시점이 퇴직일을 넘어가는 경우
        if i == N:                                      # 마지막 날이면 0
            dp[i] = 0
        else:                                           # 아니면 그 다음날 가격
            dp[i] = dp[i+1]
    else:                                               # 해당 예약종료 시점이 퇴직일을 안 넘어가는 경우
        if dp[i+1] - dp[t_lst[i]+i] > p_lst[i]:       # 상담 예약을 받았을 경우, 손해
            dp[i] = dp[i+1]                             
        else:                                           # 상담 예약을 받았을 경우, 이익
            dp[i] = dp[t_lst[i]+i] + p_lst[i] 
print(dp[1])