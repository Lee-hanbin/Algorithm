# BOJ_1922_gold4-네트워크연결

import sys
from collections import  defaultdict
from heapq import heapify, heappop, heappush

input = sys.stdin.readline

#1. kruskal
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(parent[x])
    y = find(parent[y])

    if x < y:
        parent[y] = x
    else:
        parent[x] = y 

def kruskal():

    for i in range(V + 1):
        parent[i] = i
    mst = []

    heapify(graph)

    while len(mst) < V and graph:
        w, s, e = heappop(graph)
        if find(s) != find(e):
            mst.append((s, e, w))
            union(s, e)
    return mst


#2. Prim
def prim():
    mst = []
    visited = set()

    candidate = graph_prim[1]
    visited.add(1)

    heapify(candidate)

    while len(mst) < V+1 and candidate:
        w, s, e = heappop(candidate)

        if e not in visited:
            visited.add(e)
            mst.append((w, s, e))

            for nw, ns, ne in graph_prim[e]:
                if ne not in visited:
                    heappush(candidate, (nw, ns, ne))
    return mst

V = int(input().rstrip())
E = int(input().rstrip())

graph = []
graph_prim = defaultdict(list)
parent = [-1] * (V + 1)

for _ in range(E):
    s, e, w = map(int, input().split())

    # graph.append((w, s, e))
    # graph.append((w, e, s))

    graph_prim[s].append((w, s, e))
    graph_prim[e].append((w, e, s))



# print(sum(map(lambda x: x[2], kruskal())))
print(sum(map(lambda x : x[0], prim())))