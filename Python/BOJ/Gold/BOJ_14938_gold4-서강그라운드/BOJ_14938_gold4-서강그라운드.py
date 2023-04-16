# BOJ_14938_gold4-서강그라운드

import sys
from heapq import heappop, heappush
from collections import defaultdict

input = sys.stdin.readline

#1. 구현
def dijkstra(s):
    U = {s}
    distance = [float('inf') for _ in range(n+1)]
    distance[s] = 0

    for weight, e in graph[s]:
        distance[e] = weight
    
    for _ in range(n+1):

        min_val = float('inf')

        idx = -1
        
        for i in range(n+1):
            if i not in U and min_val > distance[i]:
                min_val = distance[i]
                idx = i
        U.add(idx)

        for weight, e in graph[idx]:
            distance[e] = min(distance[e], distance[idx] + weight)
    return distance


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

# n: 지역의 개수 (노드), m: 파밍 가능 거리 r: 길의 개수 (간선)
n, m, r = map(int, input().split())

graph = defaultdict(list)
item_lst = [0] + list(map(int, input().split()))
sol = 0

for _ in range(r):
    s, e, w = map(int, input().split())

    graph[s].append((w, e))
    graph[e].append((w, s))


for i in range(1, n+1):
    tmp = 0
    # print(item_lst)
    # print(dijkstra(i))
    for idx, e in enumerate(dijkstra(i)):
        # print(idx, e)
        if e <= m:
            tmp += item_lst[idx]
    sol = max(sol, tmp)
print(sol)