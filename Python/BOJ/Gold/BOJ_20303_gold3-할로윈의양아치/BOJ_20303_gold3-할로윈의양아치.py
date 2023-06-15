# BOJ_20303_gold3-할로윈의양아치

import sys

from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
candies =[0] + list(map(int, input().split()))

graph = list([] for _ in range(n+1))

for i in range(m):
    s, e = map(int, input().split())

    graph[s].append(e)
    graph[e].append(s)

cycle = []

visited = set()

# 싸이클 개수와 사탕 개수 정하기
for i in range(1, n+1):
    cnt = 0
    candy = 0
    if i not in visited:
        que = deque()
        que.append(i)
        visited.add(i)
        while que:
            target = que.popleft()
            candy += candies[target]
            cnt += 1
            for n_target in graph[target]:
                if n_target not in visited:
                    que.append(n_target)
                    visited.add(n_target)
        cycle.append([cnt, candy])

cycle.sort(key= lambda x: (x[0], x[1]))

# 배낭 알고리즘
dp = [[0] * k for _ in range(len(cycle))]
for i in range(len(cycle)):
    for j in range(k):
        if j - cycle[i][0] >= 0:
            dp[i][j] = max(cycle[i][1] + dp[i-1][j-cycle[i][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])