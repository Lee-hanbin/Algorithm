# BOJ_2623_gold3-음악프로그램

import sys
from collections import defaultdict, deque


input = sys.stdin.readline


def topology_sort(n):
    que = deque()

    # 자식 노드가 없는 노드들 선별
    for i in range(1, n+1):
        if not indegree[i]:
            que.append(i)
    
    # 부모 노드를 체크하면서 위상정렬 진행
    res = []
    while que:
        node = que.popleft()
        res.append(node)
        for nextnode in graph[node]:
            indegree[nextnode] -= 1
            if not indegree[nextnode]:
                que.append(nextnode)

    # 정렬이 끝났는데 값이 모두 들어있지 않으면 싸이클 존재
    if len(res) < n:
        return [0]
    else:
        return res

n, m = map(int, input().split())

graph = defaultdict(list)
indegree = defaultdict(int)

for _ in range(m):
    singer = list(map(int, input().split()))[1:]
    for i in range(len(singer)-1):
        graph[singer[i]].append(singer[i + 1])
        indegree[singer[i+1]] += 1
    
sol = topology_sort(n)

for i in sol:
    print(i)