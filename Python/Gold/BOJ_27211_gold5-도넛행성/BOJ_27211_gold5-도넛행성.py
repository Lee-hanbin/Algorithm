# BOJ_27211_gold5-도넛행성

import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

# 바운더리 연결
# def boundary(rc, num):
#     if rc == 1:             # rc 가 1이면 row
#         if num == -1:
#             return num + N
#         return num % N
#     else:                   # rc 가 2이면 column
#         if num == -1:
#             return num + M
#         return num % M
    
def bfs():
    cnt = 0
    que = deque()
    visited = set()
    while zero_set:
        cnt += 1
        r, c = zero_set.pop()
        que.append((r, c))
        visited.add((r, c))
        while que:
            r, c = que.popleft()
            for i in range(4):
                # nr = boundary(1, dr[i] + r)
                # nc = boundary(2, dc[i] + c)
                nr = (dr[i] + r) % N
                nc = (dc[i] + c) % M
                if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited:
                    if not map1[nr][nc]:            # 숲이 아니면 que에 넣기
                        que.append((nr, nc))
                        zero_set.discard((nr, nc))
                    visited.add((nr, nc))
    return cnt


N, M = map(int, input().split())

map1 = []
zero_set = set()

for i in range(N):
    map1.append(list(map(int, input().split())))
    for j, e in enumerate(map1[i]):
        if e == 0:
            zero_set.add((i, j))

print(bfs())