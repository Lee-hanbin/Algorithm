# BOJ_2096_gold5-내려가기

import sys

input = sys.stdin.readline

n = int(input())

# map1 = [list(map(int, input().split())) for _ in range(n)]

# 풀이1
# dp = [[[0,0]] * 3 for _ in range(n)]
#
# dp[0][0]  = map1[0][0], map1[0][0] 
# dp[0][1]  = map1[0][1], map1[0][1]
# dp[0][2]  = map1[0][2], map1[0][2]
#
# for i in range(1, n):
#     dp[i][0] = max(dp[i-1][0][0], dp[i][1][0]) + map1[i][0] , min(dp[i-1][0][1], dp[i-1][1][1]) + map1[i][0]
#     dp[i][1] = max(dp[i-1][0][0], dp[i-1][1][0], dp[i-1][2][0]) + map1[i][1], min(dp[i-1][0][1], dp[i-1][1][1], dp[i-1][2][1]) + map1[i][1]
#     dp[i][2] = max(dp[i-1][1][0], dp[i-1][2][0]) + map1[i][2], min(dp[i-1][1][1], dp[i-1][2][1]) + map1[i][2]
#
# print(max(dp[-1][0][0], dp[-1][1][0], dp[-1][2][0]), min(dp[-1][0][1], dp[-1][1][1], dp[-1][2][1]))


# 풀이2
# dp_min = [[0] * 3 for _ in range(n)]
#
# dp_max[0][0] = dp_min[0][0] = map1[0][0]
# dp_max[0][1] = dp_min[0][1] = map1[0][1]
# dp_max[0][2] = dp_min[0][2] = map1[0][2]
#
# for i in range(1, n):
#     dp_max[i][0] = max(dp_max[i-1][0], dp_max[i][1]) + map1[i][0]
#     dp_max[i][1] = max(dp_max[i-1]) + map1[i][1]
#     dp_max[i][2] = max(dp_max[i-1][1], dp_max[i-1][2]) + map1[i][2]

#     dp_min[i][0] = min(dp_min[i-1][0], dp_min[i-1][1]) + map1[i][0]
#     dp_min[i][1] = min(dp_min[i-1]) + map1[i][1]
#     dp_min[i][2] = min(dp_min[i-1][1], dp_min[i-1][2]) + map1[i][2]
#
# print(max(dp_max[-1]), min(dp_min[-1]))


# 풀이3

# before_max_dp = map1[0]
# sol_max_dp = [0] * 3

# before_min_dp = map1[0]
# sol_min_dp = [0] * 3

# for i in range(1, n):
#     sol_max_dp[0] = max(before_max_dp[0], before_max_dp[1]) + map1[i][0]
#     sol_max_dp[1] = max(before_max_dp) + map1[i][1]
#     sol_max_dp[2] = max(before_max_dp[1], before_max_dp[2]) + map1[i][2]
#     before_max_dp = sol_max_dp[::]

#     sol_min_dp[0] = min(before_min_dp[0], before_min_dp[1]) + map1[i][0]
#     sol_min_dp[1] = min(before_min_dp) + map1[i][1]
#     sol_min_dp[2] = min(before_min_dp[1], before_min_dp[2]) + map1[i][2]
#     before_min_dp = sol_min_dp[::]

# print(max(sol_max_dp), min(sol_min_dp))

# 풀이4
for i in range(n):
    map1 = list(map(int,input().split()))
    if i == 0:
        sol_max_dp = map1[::]
        sol_min_dp = map1[::]
        before_max_dp = map1[::]
        before_min_dp = map1[::]
    else:
        sol_max_dp[0] = max(before_max_dp[0], before_max_dp[1]) + map1[0]
        sol_max_dp[1] = max(before_max_dp) + map1[1]
        sol_max_dp[2] = max(before_max_dp[1], before_max_dp[2]) + map1[2]
        before_max_dp = sol_max_dp[::]

        sol_min_dp[0] = min(before_min_dp[0], before_min_dp[1]) + map1[0]
        sol_min_dp[1] = min(before_min_dp) + map1[1]
        sol_min_dp[2] = min(before_min_dp[1], before_min_dp[2]) + map1[2]
        before_min_dp = sol_min_dp[::]

print(max(sol_max_dp), min(sol_min_dp))