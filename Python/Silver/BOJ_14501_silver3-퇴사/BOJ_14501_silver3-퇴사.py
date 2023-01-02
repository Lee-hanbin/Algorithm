# BOJ_14501_silver3-퇴사
import sys
input = sys.stdin.readline
n = int(input().strip())


# 풀이 1 (바텀업)
# lst = []
# dp = [0]*(n+5)
# for i in range(n):
#     t, p = map(int,input().split())
#     lst.append((t, p))
# for i in range(n-1, -1, -1):
#     if lst[i][0] + i <= n:        # n을 넘어가지 않게 함
#         dp[i] = max(lst[i][1] + dp[i + lst[i][0]], dp[i+1])
#     else:
#         dp[i] = dp[i+1]
# print(dp[0])

# 풀이 2 (탑다운)
lst = [(0,0)]
dp = [0]*(n+1)

for i in range(1, n+1):
    t, p = map(int,input().split())
    lst.append((t, p))

for i in range(1, n+1):
    time = lst[i][0]                # 기간
    price = lst[i][1]               # 금액
    if time + i <= n+1:             # n일 이내에만
        dp[i] = max(dp[i], price)   # 현재 금액과 새로운 금액 중 큰 것으로 우선 할당
        for j in range(i+time, n+1):    # 그 이후에 예약에 대한 금액 변경
            nt = lst[j][0]              # 새로운 예약 기간
            if j + nt <= n+1:           # 새로운 예약 기간이 n일 이내
                dp[j] = max(dp[j], lst[j][1]+dp[i]) # 갱신
    print(dp)
print(max(dp))