# BOJ_4386_gold3-별자리만들기

import sys
from itertools import combinations
from collections import defaultdict
from heapq import heapify, heappop, heappush
input = sys.stdin.readline


# 두 점 사이의 거리 공식
def distance_f(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 )**0.5

# 다각형의 대각선 수 공식
def polygon_diagonal_f(m):
    if m <3:
        return m-1
    elif m == 3:
        return 3
    else:
        return m*(m-3)//2

# # Prim_general
# def Prim(s):
#     visited = [0] *(V+1)
#     key = [float('inf')] *(V+1) 
#     parent = [-1] * (V+1)
#     key[s] = 0
#     for _ in range(V+1):
#         min_v = float('inf') 

#         for i in range(V+1):
#             if visited[i] == 0 and key[i] < min_v:
#                 s = i
#                 min_v = key[i]
#         visited[s] = 1
#         for e,w in graph[s]:
#             if visited[e] == 0 and key[e] > w:
#                 key[e] = w
#                 parent[e] = s
#     return sum(key[:-1])

# Prim_heapq
def Prim(s):
    mst = []
    visited = {s}
    candidate = graph[s]
    heapify(candidate)
    while len(visited) < V+1 and candidate:
        w, s, e = heappop(candidate)
        if e not in visited:
            visited.add(e)
            mst.append((w,s,e))
            for rough in graph[e]:
                if rough[2] not in visited:
                    heappush(candidate, rough)
    return sum(map(lambda x: x[0],mst))


n = int(input())

lst = [0] * n
graph = defaultdict(list)

for i in range(n):
    x, y = map(float,input().split())
    lst[i] = (x,y,i)

V = n                       # node의 개수
E = polygon_diagonal_f(n)   # 간선의 개수
if E == 0:
    print(0)
elif E == 1:
    print(distance_f(lst[0],lst[1]))
else:
    # 그래프 생성
    for i in combinations(lst,2):
        p1, p2 = i
        s, e, w = p1[2], p2[2], distance_f(p1, p2)
        # graph[s].append((e,w))
        # graph[e].append((s,w))
        graph[s].append((w,s,e))
        graph[e].append((w,e,s))
    print(round(Prim(0),2))
    # print(Prim(0))








'''
6
4 1
5 8
2 1
8 4
2 9
1 4
'''