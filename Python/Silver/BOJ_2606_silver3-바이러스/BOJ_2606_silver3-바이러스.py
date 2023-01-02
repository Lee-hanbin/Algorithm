# BOJ_2606_silver3-바이러스

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
graph = defaultdict(list)
for _ in range(k):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

que = deque()
que.append(1)
visited = set()
while que:
    v = que.popleft()
    if v in visited:
        continue
    visited.add(v)
    for i in graph[v]:
        if i not in visited:
            # cnt += 1
            que.append(i)
print(len(visited)-1)