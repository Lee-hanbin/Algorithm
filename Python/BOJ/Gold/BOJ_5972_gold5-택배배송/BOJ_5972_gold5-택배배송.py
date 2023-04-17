# BOJ_5972_gold5-택배배송

import sys
from heapq import heappop, heappush
from collections import defaultdict

input = sys.stdin.readline

def djikstra(start):
    hq = []
    distance[start] = 0

    # 시작 비용과 시작점을 큐에 넣는다.
    heappush(hq, [0, start])

    while hq:
        cost, node = heappop(hq)

        # 해당 헛간에 연결되어 있는 모든 헛간을 체크 한다.
        for next_cost, next_node in graph[node]:
            next_cost += cost

            # 갱신된 헛간 사이의 비용이 기존의 경로보다 작으면 최소비용 갱신
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heappush(hq, [next_cost, next_node])

    return distance[-1]
V, E = map(int, input().split())

graph = defaultdict(list)
distance = [float('inf')] * (V + 1)

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
    graph[e].append((w, s))

print(djikstra(1))