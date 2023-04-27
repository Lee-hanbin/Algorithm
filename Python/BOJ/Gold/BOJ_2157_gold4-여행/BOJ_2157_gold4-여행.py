# BOJ_2157_gold4-여행

import sys
from collections import defaultdict

input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = defaultdict(list)

for _ in range(k):
    s, e, w = map(int, input().split())
    if s < e:
        graph[s].append((e, w))

dp = [[0] * (m+1) for _ in range(n+1)]


# 1번 도시에서 출발하는 도시 체크
for e, w in graph[1]:
    dp[e][2] = max(dp[e][2], w)

# 최대 m번 거쳐서 갈 수 있는 도시들 체크
for j in range(2, m):
    for i in range(2, n + 1):
        # 앞에 시작점이 있어야지 의미가 있으므로
        if dp[i][j] > 0:
            tmp = dp[i][j]
            # i번째 도시에서 출발해서 도착할 수 있는 도시들 체크
            for e, w in graph[i]:
                dp[e][j+1] = max(dp[e][j+1], tmp + w)


print(max(dp[n]))