# BOJ_11779_gold3-최소비용구하기2

import sys
from heapq import heappop, heappush
from collections import defaultdict

input = sys.stdin.readline


#2. heapq 이용

def dijkstra(node):
    dist = [float('inf')] * (V+1)
    dist[node] = 0
    hq = []
    heappush(hq, [0, node])

    while hq:
        now_w, now_v = heappop(hq)
        if dist[now_v] < now_w:
            continue
        for w, v in graph_di[now_v]:
            w += now_w
            if w < dist[v]:
                dist[v] = w
                heappush(hq, [w, v])
                dist2[v] = now_v
    return dist


V = int(input())
E = int(input())
graph_di = defaultdict(list)
for _ in range(E):
    s, e, weight = map(int,input().split())
    graph_di[s].append((weight, e))
    # graph_di[e].append((weight, s))

start, end = map(int, input().split())
dist2 = [ i for i in range(V+1)]

print(dijkstra(start)[end])

path = []
tmp = end
while 1:
    path.append(tmp)
    if tmp == dist2[tmp]:
        break
    tmp = dist2[tmp]

print(len(path))
print(*(path[::-1]))