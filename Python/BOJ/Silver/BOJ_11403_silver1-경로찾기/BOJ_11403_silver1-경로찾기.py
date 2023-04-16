# BOJ_11403_silver1-경로찾기

import sys
from collections import deque
input = sys.stdin.readline


def bfs(s):
    que = deque()
    visited = [0] * n
    que.append(s)
    while que:
        start = que.popleft()
        for i, e  in enumerate(graph[start]):
            if e and not visited[i]:
                visited[i] = 1
                que.append(i)
    return visited

n = int(input().rstrip())

graph = [list(map(int, input().split())) for _ in range(n)]
sol_lst = [0] * n


for i in range(n):
    print(*bfs(i))
