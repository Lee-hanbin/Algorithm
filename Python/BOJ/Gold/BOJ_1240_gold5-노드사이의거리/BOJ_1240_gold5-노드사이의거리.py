# BOJ_1240_gold5-노드사이의거리

import sys
from collections import defaultdict
from heapq import heappop, heappush

input = sys.stdin.readline

def djikstra(node):
    dist = [float('inf')] * (n + 1)
    hq = []
    dist[node] = 0
    heappush(hq, [0, node])
    
    while hq:
        current_dist, current_node = heappop(hq)
        
        for next_dist, next_node in graph[current_node]:
            next_dist += current_dist
            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                heappush(hq, [next_dist, next_node])

    return dist

n, m = map(int, input().split())

graph = defaultdict(list)
for _ in range(1, n):
    s, e ,c = map(int, input().split())
    graph[s].append([c, e])
    graph[e].append([c, s])
    
for i in range(m):
    startNode, endNode = map(int, input().split())
    print(djikstra(startNode)[endNode])