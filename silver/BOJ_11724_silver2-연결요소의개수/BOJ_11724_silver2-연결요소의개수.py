# BOJ_11724_silver2-연결요소의개수

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def  bfs(s):
    que = deque()
    que.append(s)
    visited.add(s)
    while que:
        node = que.popleft()
        for i in graph[node]:
            if i not in visited:
                que.append(i)
                visited.add(i)


graph = defaultdict(list)

V, E = map(int, input().split())

for i in range(E):
    s, e = map(int, input().split())

    graph[s].append(e)
    graph[e].append(s)

visited = set()
cnt = 0

for i in range(1, V+1):
    if i not in visited:
        cnt += 1
        bfs(i)

print(cnt)