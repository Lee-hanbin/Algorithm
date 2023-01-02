# BOJ_12865_gold5-평범한배낭

from collections import deque
from copy import copy
import sys
input = sys.stdin.readline

def bfs():
    que = deque()
    visited = set()
    for i in lst:
        pack = set()
        pack.add(i)
        que.append([pack, i[0], i[1]])
        # visited.add(pack)
    while que:
        chk_pack, chk_w, val_sum = que.popleft()
        if chk_pack in visited:
            continue
        visited.add(chk_pack)
        for i in lst:
            if chk_w+i[0] > k:
                sol.append(val_sum)
                continue
            if i not in chk_pack:
                tmp = copy(chk_pack)
                tmp.add(i)
                que.append([tmp, chk_w+i[0], val_sum+i[1]])

n, k = map(int,input().split())
lst = []
sol = []
for _ in range(n):
    w, v = map(int,input().split())
    if w < k:
        lst.append((w,v))
bfs()

print(max(sol))