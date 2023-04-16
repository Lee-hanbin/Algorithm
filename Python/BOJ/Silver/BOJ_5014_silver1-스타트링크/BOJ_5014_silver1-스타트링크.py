# BOJ_5014_silver1-스타트링크

import sys
from collections import deque

input = sys.stdin.readline


def bfs(Final, Start, Goal):
    visited = [0] * (Final + 1)
    que = deque()
    cnt = 0
    que.append((Start, cnt))
    visited[Start] = 1

    while que:
        now, cnt = que.popleft()
        if now == Goal:
            return cnt
        
        if now + U <= Final and not visited[now + U]:
            visited[now+U]=1
            que.append((now + U, cnt + 1))

        if now - D >= 1 and not visited[now - D]:
            que.append((now - D, cnt + 1))
            visited[now-D]=1

    return "use the stairs"

F, S, G, U, D = map(int, input().split())

print(bfs(F, S, G))

