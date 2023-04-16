# BOJ_2252_gold3-줄세우기

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

que= deque()
line = [[] for _ in range(n+1)]
cnt_chk = [0] * (n+1)


for i in range(m):
    s, e = map(int, input().split())
    line[s].append(e)
    cnt_chk[e] += 1

sol = []

for i in range(1, n+1):
    if not cnt_chk[i]:
        que.append(i)


while que:
    node = que.popleft()
    sol.append(node)
    
    for next in line[node]:
        cnt_chk[next] -= 1
        if not cnt_chk[next]:
            que.append(next)

print(*sol)