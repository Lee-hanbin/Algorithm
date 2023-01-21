import sys

input = sys.stdin.readline

INF = int(5000 * 10000) # 무한대 값

# 벨만-포드 알고리즘
def bellmanFord(start):

    # 최단거리 테이블을 무한대로 초기화
    distance = [INF] * (N + 1)
    # 시작 노드에 대해서 초기화
    distance[start] = 0

    # N번 edge relaxation을 반복.
    for i in range(N):
        for curNode, nextNode, edgeCost in graph:
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[curNode] + edgeCost < distance[nextNode]:
                distance[nextNode] = distance[curNode] + edgeCost
                # N번째 반복에서 갱신되는 값이 있으면 Negative cycle 존재
                if i == N - 1:
                    return True

    # 벨만-포드 정상종료
    return False


for _ in range(int(input())):
    graph = []
    N, M, W = map(int, input().split())
    for _ in range(M):
        s, e, t = map(int, input().split())
        graph.append((s, e, t))
        graph.append((e, s, t))
    for _ in range(W):
        s, e, t = map(int, input().split())
        graph.append((s, e, -t))


    if bellmanFord(1):
        print('YES')
    else:
        print('NO')
