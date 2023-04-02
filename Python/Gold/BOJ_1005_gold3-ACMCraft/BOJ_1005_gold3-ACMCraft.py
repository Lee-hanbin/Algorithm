import sys
from collections import deque
input = sys.stdin.readline


def topology_sort(final):
    q = deque()

    # 도착지가 되는 간선이 존재하지 않는 노드를 모두 큐에 넣고 비용(시간) 체크
    for i in range(1, v+1):
        if not indegree[i]:
            q.append(i)
            dp[i] = cost[i-1]
    
    # 큐가 비거나, 목적지의 건설이 시작되기 전까지 반복
    while q and indegree[final]:
        now = q.popleft()

        # 목적지가 없거나 이미 연결된 노드들로 부터 뻗어나가는 간선에 연결된 노드의 연결을 끊고
        # 해당 연결이 끊겼을 때, 더 이상 연결되는 간선이 없으면 해당 노드를 큐에 넣는다.
        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[now] + cost[i-1], dp[i])
            if not indegree[i]:
                q.append(i)
    
    # 목적지까지 모든 노드가 연결되면 해당 비용(시간)을 출력
    print(dp[final])

T = int(input())

for _ in range(T):
    v, e = map(int,input().split())
    cost = list(map(int,input().split()))
    graph = [[] for _ in range(v+1)]
    indegree = [0] * (v+1)
    dp = [0 for _ in range(v + 1)]

    # 모든 도착지에 도달하는 간선의 개수를 체크
    for _ in range(e):
        s, e = map(int,input().split())
        graph[s].append(e)
        indegree[e] += 1

    W = int(input())
    
    # 위상 정렬
    topology_sort(W)