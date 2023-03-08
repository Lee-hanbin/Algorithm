# BOJ_1504_gold4-특정한최단거리찾기

from collections import defaultdict
import sys

input = sys.stdin.readline

# 1. 다익스트라 구현

def dijkstra(s):
    U = {s}
    distance = [float('inf') for _ in range(V+1)]
    distance[s] = 0

    for e, weight in graph_di[s]:
        distance[e] = weight
    
    for _ in range(V+1):

        min_val = float('inf')

        idx = -1
        
        for i in range(V+1):
            if i not in U and min_val > distance[i]:
                min_val = distance[i]
                idx = i
        U.add(idx)

        for e, weight in graph_di[idx]:
            distance[e] = min(distance[e], distance[idx] + weight)
    return distance

V, E = map(int,input().split())
graph_di = defaultdict(list)

for _ in range(E):
    s, e, weight = map(int,input().split())
    graph_di[s].append((e,weight))
    graph_di[e].append((s,weight))

v1, v2 = map(int, input().split())
sol = float('inf')

distance_v1 = dijkstra(v1)
distance_v2 = dijkstra(v2)
distance_all = dijkstra(1)

sol = min(distance_all[v1]+ distance_v1[v2] + distance_v2[V], distance_all[v2] + distance_v2[v1] + distance_v1[V])

if sol >= float('inf'):
    print(-1)
else:
    print(sol)


#2. heapq를 이용한 다익스트라

import heapq

def dijkstra(node):
    dist = [float('inf')] * (V+1)
    dist[node] = 0
    hq = []
    heapq.heappush(hq, [0, node])

    while hq:
        now_w, now_v = heapq.heappop(hq)
        for w, v in graph_di[now_v]:
            w += now_w
            if w < dist[v]:
                dist[v] = w
                heapq.heappush(hq, [w, v])
    return dist


V, E = map(int,input().split())
graph_di = defaultdict(list)

for _ in range(E):
    s, e, weight = map(int,input().split())
    graph_di[s].append((weight, e))
    graph_di[e].append((weight, s))

v1, v2 = map(int, input().split())
sol = float('inf')

distance_v1 = dijkstra(v1)
distance_v2 = dijkstra(v2)
distance_all = dijkstra(1)

sol = min(distance_all[v1]+ distance_v1[v2] + distance_v2[V], distance_all[v2] + distance_v2[v1] + distance_v1[V])

if sol >= float('inf'):
    print(-1)
else:
    print(sol)
