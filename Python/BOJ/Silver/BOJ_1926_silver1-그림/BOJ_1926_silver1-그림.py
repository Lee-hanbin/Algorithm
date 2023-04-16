# BOJ_1926_silver1-그림

import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

n, m = map(int, input().split())
map1 = [list(map(int,input().split())) for _ in range(n)]
set_one_store = set()

picture_count = 0
picture_size_list = []


for r in range(n):
    for c in range(m):
        if map1[r][c] == 1:
            set_one_store.add((r,c))
if len(set_one_store) == 0:
    print(0)
    print(0)
    exit()

que = deque()
while set_one_store:
    r, c = set_one_store.pop()
    visited = set()
    picture_size = 1                   # 그림의 크기
    picture_count += 1                 # 그림의 개수
    que.append((r,c))
    visited.add((r,c))
    while que:
        r, c  = que.popleft()
        set_one_store.discard((r,c))
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if (nr,nc) not in visited and 0 <= nr < n and 0 <= nc < m and map1[nr][nc] == 1:
                picture_size += 1
                visited.add((nr,nc))
                que.append((nr,nc))
    picture_size_list.append(picture_size)

print(picture_count)
print(max(picture_size_list))
