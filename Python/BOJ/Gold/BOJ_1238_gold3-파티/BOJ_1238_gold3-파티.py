# BOJ_1238_gold3-파티

import sys
from heapq import heappop, heappush
from collections import defaultdict

def dijkstra(node):
    dist = [float('inf')] * (n+1)
    dist[node] = 0
    hq = []
    heappush(hq, [0, node])

    while hq:
        now_w, now_v = heappop(hq)
        for w, v in graph[now_v]:
            w += now_w
            if w < dist[v]:
                dist[v] = w
                heappush(hq, [w, v])
    return dist


input = sys.stdin.readline

n, m, x = map(int, input().split())

graph = defaultdict(list)
idx_lst = [0] * (n+1)

for i in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))

x_dist = dijkstra(x)

for i, e in enumerate(x_dist):
    if i != float('inf') and i:
        idx_lst[i] = 1

sol = 0

for i, e in enumerate(idx_lst):
    if e:
        sol = max(sol, dijkstra(i)[x] + x_dist[i])

print(sol)