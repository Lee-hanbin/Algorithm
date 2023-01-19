# BOJ_9663_gold4-NQUEEN

import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

def bfs(idx):
    s_r, e_r = idx
    que = deque()
    visited = set()
    que.append(idx)
    visited.add(idx)
    while que:
        r, c = que.popleft()
        for i in range(s_r, n):
            for j in range(n):
                if 

n = int(input().split())

map1 = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        bfs((i, j))