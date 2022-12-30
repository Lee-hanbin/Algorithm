# BOJ_1946_gold4-운동
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

# 1. heapq
# def dijkstra(node):
#     dist = [float('inf')] * (V+1)
#     dist[node] = 0
#     hq = []
#     heapq.heappush(hq, [0, node])

#     while hq:
#         now_w, now_v = heapq.heappop(hq)
#         for w, v in graph_di[now_v]:
#             w += now_w
#             if w < dist[v]:
#                 dist[v] = w
#                 heapq.heappush(hq, [w, v])
#     return dist[1:]

# 2. 구현
def dijkstra(s):
    U = {s}
    distance = [float('inf') for _ in range(V+1)]
    distance[s] = 0
    for e, weight in graph_di[s]:
        distance[e] = weight
    
    for _ in range(V+1):

        min_val = float('inf')

        idx = -1                                            # ㅕ

        for i in range(V+1):
            if i not in U and min_val > distance[i]:
                min_val = distance[i]
                idx = i
        if idx > -1:
            U.add(idx)
        else:
            continue

        for e, weight in graph_di[idx]:
            distance[e] = min(distance[e], distance[idx] + weight)
    return distance[1:]

V, E = map(int,input().split())
graph_di = defaultdict(list)

store_lst = []
sol_lst = []

for _ in range(E):
    s, e, weight = map(int,input().split())
    if s == e:
        sol_lst.append(weight)
    # graph_di[s].append((e,weight))
    graph_di[s].append((weight, e))


for i in range(1, V+1):
    chk = dijkstra(i)
    store_lst.append(chk)

for s in range(V):
    for j in range(V):
        if j == s:
            continue
        if store_lst[s][j] != float('inf') and store_lst[j][s] != float('inf'):
            sol_lst.append(store_lst[s][j] + store_lst[j][s])
if sol_lst:
    print(min(sol_lst))
else:
    print(-1)