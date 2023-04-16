# BOJ_9205_gold5-맥주마시면서걸어가기

import sys

from collections import deque

input = sys.stdin.readline

def bfs():
    que = deque()
    visited = set()
    que.append((sr, sc))
    visited.add((sr, sc))
    while que:
        r, c = que.popleft()
        for nr, nc in shop:
            if abs(r - nr) + abs(c - nc) <= 1000 and (nr, nc) not in visited:
                if abs(nr - er) + abs(nc - ec) <= 1000:
                    return 'happy'
                que.append((nr, nc))
                visited.add((nr, nc))
    return 'sad' 

t = int(input())

for _ in range(t):
    n = int(input())
    sr, sc = map(int, input().split())
    shop = [0] * n
    for i in range(n):
        shop_r, shop_c = map(int, input().split())
        shop[i] = (shop_r, shop_c)
    er, ec = map(int, input().split())
    if abs(sr - er) + abs(sc - ec) <= 1000:
        print("happy")
    else:
        print(bfs())