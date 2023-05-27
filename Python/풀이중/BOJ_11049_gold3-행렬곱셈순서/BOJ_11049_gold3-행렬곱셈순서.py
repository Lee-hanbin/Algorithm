# BOJ_11049_gold3-행렬곱셈순서

import sys

input = sys.stdin.readline
N = int(input())

nums = list(map(int, input().split()))
for _ in range(N-1):
    _, c = map(int, input().split())
    nums.append(c)

# DP
dp = [[0]*N for _ in range(N)]
for d in range(N):
    for i in range(N - d):
        j = i + d

        if i == j:
            continue

        dp[i][j] = float('inf')
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1]
                            [j] + nums[i]*nums[k+1]*nums[j+1])

print(dp[0][-1])
# n = int(input())

# matrix_lst = list(list(map(int, input().split())) for _ in range(n))
# index_lst = [0] * (n-1)
# index_set = set()
# sol = 0 

# for i in range(n-1):
#     index_lst[i] = [matrix_lst[i][1], i+1, matrix_lst[i][0]]

# index_lst.sort(key=lambda x: (-x[0], -x[2]))

# for m, idx, tmp in index_lst:
#     r = idx - 1
#     c = idx
#     while r in index_set:
#         r -= 1 
#     while c in index_set:
#         c += 1
#     sol += matrix_lst[r][0] * m * matrix_lst[idx][1]
#     index_set.add(idx)
#     matrix_lst[r][1] = matrix_lst[idx][1]
#     matrix_lst[idx][0] = matrix_lst[r][0]
# print(sol)
