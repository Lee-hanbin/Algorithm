# BOJ_2887_Platinum5-행성터널

import sys
from heapq import heapify, heappop, heappush
from collections import defaultdict

from pprint import pprint

input = sys.stdin.readline

# Prim_heapq
def Prim(s):
    mst = []
    visited = {s}
    candidate = graph[s]
    heapify(candidate)
    while len(visited) < n+1 and candidate:
        w, s, e = heappop(candidate)
        if e not in visited:
            visited.add(e)
            mst.append((w,s,e))
            for rough in graph[e]:
                if rough[2] not in visited:
                    heappush(candidate, rough)
    return sum(map(lambda x: x[0],mst))

# 2. Prim 구현
# def Prim(node):
#     visited = [0]*(n)
#     key = [float('inf')]*(n)
#     parent = [-1]*(n)
#     key[node] = 0
#     for _ in range(n):
#         min_val = float('inf')
#         for i in range(n):
#             if visited[i]==0 and key[i] < min_val:
#                 s = i
#                 min_val = key[i]
#         visited[s] = 1

#         for e in range(n):
#             if visited[e] == 0 and graph[s][e] > -1:
#                 if key[e] > graph[s][e]:
#                     key[e] = graph[s][e]
#                     parent[e] = s
#     return sum(key)
#     # return key



# 3.  kruskal, 우선순위 큐
# def make_set(x):
#     parent[x] = x
#     rank[x] = 0             # 효율적인 link를 위해서 필요
#                             # 연결했을 때, 랭크가 늘어나지 않는 경우를 만들기 위해

# def find_set(x):
#     while x != parent[x]:
#         x = parent[x]
#     return parent[x]

# def union(x,y):
#     link(find_set(x), find_set(y))
#     # 루트끼리만 비교하는 것!!!!!

# def link(x,y):
#     if rank[x] > rank[y]:
#         parent[y] = x
#     else:
#         parent[x] = y
#         if rank[x] == rank[y]:
#             rank[y] += 1


# def mst_kruskal2():

#     mst = []

#     for i in range(n):
#         make_set(i)
#     chk = [x[::-1] for x in graph]
#     heapify(chk)

#     while len(mst) < n-1 and chk:
#         weight, e, s = heappop(chk)
#         if find_set(s) != find_set(e):
#             mst.append((weight,s,e))
#             union(s,e)
#     # print(mst)
#     return sum(map(lambda x : x[0], mst))


n = int(input())

# parent = [-1]*(n)
# rank = [-1]*(n)  

# idx_lst = [list(map(int, input().split())) + [i] for i in range(n)]
idx_lst = [[0]*n for _ in range(3)]
for i in range(n):
    x, y, z = map(int, input().split())
    idx_lst[0][i] = (x, i) 
    idx_lst[1][i] = (y, i)
    idx_lst[2][i] = (z, i)
graph = defaultdict(list)
# graph = [[0]*n for _ in range(n)]
# graph = []

for i in range(3):          # x축, y축, z축 정렬
    idx_lst[i].sort()


for i in range(n-1):
    for j in range(3):      # 각 축에 정렬된 값들에 이웃된 행성만 간선으로 연결
        idx = idx_lst[j]
        w = abs(idx[i+1][0] - idx[i][0])
        graph[idx[i][1]].append((w, idx[i][1], idx[i+1][1]))
        graph[idx[i+1][1]].append((w, idx[i+1][1], idx[i][1]))

pprint(graph)
# for i in range(n):
#     x1, y1, z1 = idx_lst[i]
#     for j in range(i+1, n):
#         x2, y2, z2 = idx_lst[j]
#         w = min(abs(x1-x2), abs(y1-y2), abs(z1-z2))
#         graph[i].append((w, i, j))
#         graph[j].append((w, j, i))
#         # graph.append([i,j,w])
# pprint(graph)
print(Prim(0))
# print(mst_kruskal2())