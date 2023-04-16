# BOJ_1647_gold4-도시분할계획

import sys
from collections import defaultdict

from heapq import heappop, heappush, heapify
input = sys.stdin.readline

def prim2(node):
    
    mst = []
    visited = {node}

    candidate = graph_list[node]
    heapify(candidate)

    while len(visited) < V+1 and candidate :
        weight, s, e = heappop(candidate)

        if e not in visited:
            visited.add(e)
            mst.append(weight)

            for route in graph_list[e]:
                if route[2] not in visited:
                    heappush(candidate, route)

    mst.sort()
    mst.pop()
    return sum(mst)



V, E = map(int,input().split())
graph_list = defaultdict(list)

for _ in range(E):
    s, e, weight = map(int,input().split())
    graph_list[s].append((weight,s,e))
    graph_list[e].append((weight,e,s))


print(prim2(1))