# BOJ_12852_silver1-1로 만들기2

import sys
from collections import deque

input = sys.stdin.readline

def bfs(num):
    que = deque()
    visited = set()
    que.append((0, num, [num]))
    visited.add(num)
    while que:
        cnt, chk, cul_lst = que.popleft()

        # 3으로 나누어 떨어지고 방문하지 않았으면 que에 넣기
        if not chk % 3:
            nxt_num1 = chk//3
            if nxt_num1 not in visited:
                que.append((cnt + 1, nxt_num1, cul_lst+[nxt_num1]))
                visited.add(nxt_num1)
                if nxt_num1 == 1:
                    return cnt+1, cul_lst +[nxt_num1]
        # 2로 나누어 떨어지고 방문하지 않았으면 que에 넣기
        if not chk % 2:
            nxt_num2 = chk//2
            if nxt_num2 not in visited:
                que.append((cnt + 1, nxt_num2, cul_lst+[nxt_num2]))
                visited.add(nxt_num2)
                if nxt_num2 == 1:
                    return cnt+1, cul_lst +[nxt_num2]
        # 1을 뺐을 때, 0보다 큰 경우에만 que에 넣기
        nxt_num3 = chk - 1
        if nxt_num3 > 0 and nxt_num3 not in visited:
            que.append((cnt + 1, nxt_num3, cul_lst+[nxt_num3]))
            visited.add(nxt_num3)
            if nxt_num3 == 1:
                return cnt+1, cul_lst +[nxt_num3]



n = int(input())

if n == 1:
    print(0)
    print(1)
    exit()

cnt, lst = bfs(n)
print(cnt)
print(*lst)