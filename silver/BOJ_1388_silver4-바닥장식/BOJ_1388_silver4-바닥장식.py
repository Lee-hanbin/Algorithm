# BOJ_1388_silver4-바닥장식

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

map1 = [list(input().rstrip()) for _ in range(n)]

k = 0

for i in range(n):
    for j in range(m):
        # 가로 나무 판자인 경우
        if map1[i][j] == '-':                   
            if j+1 == m:                # 끝의 판자인 경우 +1
                k+=1
            else:                       # 끝의 판자가 아닌 경우
                if map1[i][j+1] == '-': # 다음 판자에 -가 오면 그대로
                    continue
                else:                   # 다음 판자에 -가 안 오면 +1
                    k+=1
        # 세로 나무 판자인 경우
        else:
            if i+1 == n:                # 끝의 판자인 경우 +1
                k+=1
            else:                       # 끝의 판자가 아닌 경우
                if map1[i+1][j] == '|': # 다음 판자에 |가 오면 그대로
                    continue
                else:                   # 다음 판자에 |가 안 오면 +1
                    k+=1
        
print(k)

# dp = [0] * n * m
# k = 0

# for i in range(n):
#     for j in range(m):
#         # 가로 나무 판자인 경우
#         if map1[i][j] == '-':                   
#             if j+1 == m:                # 끝의 판자인 경우 +1
#                 dp[k] = dp[k-1] + 1
#             else:                       # 끝의 판자가 아닌 경우
#                 if map1[i][j+1] == '-': # 다음 판자에 -가 오면 그대로
#                     dp[k] = dp[k-1]
#                 else:                   # 다음 판자에 -가 안 오면 +1
#                     dp[k] = dp[k-1] + 1
#         # 세로 나무 판자인 경우
#         else:
#             if i+1 == n:                # 끝의 판자인 경우 +1
#                 dp[k] = dp[k-1] + 1
#             else:                       # 끝의 판자가 아닌 경우
#                 if map1[i+1][j] == '|': # 다음 판자에 |가 오면 그대로
#                     dp[k] = dp[k-1]
#                 else:                   # 다음 판자에 |가 안 오면 +1
#                     dp[k] = dp[k-1] + 1
#         k+=1
# print(dp[-1])