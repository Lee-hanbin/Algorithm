# BOJ_9019_gold4_DSLR

import sys
from collections import deque

input = sys.stdin.readline

def zero_chk(num):
    num = str(num)
    for _ in range(3):
        if len(num) < 4:
            num = '0' + num
        else:
            break
    return num

def bfs(before, after):
    que = deque()
    # visited = set()
    visited = [0] * 10000
    if before < 1000:
        before = zero_chk(before)
    before = str(before)
    que.append((before, ''))
    # visited.add(before)
    visited[int(before)] = 1
    while que:
        num, command = que.popleft()
        # print(num)
        for c in ['D', 'S', 'L', 'R']:
            if c == 'D':
                next_num = (int(num) * 2) % 10000
                if next_num < 1000:
                    next_num = zero_chk(next_num)
                next_num = str(next_num)
            elif c == 'S':
                next_num = ((int(num) - 1) + 10000) % 10000 
                if next_num < 1000:
                    next_num = zero_chk(next_num)
                next_num = str(next_num)
            elif c == 'L':
                next_num = num[1:] + num[:1]
            else:
                next_num  = num[3:] + num[:3]
            if int(next_num) == after:
                return command + c
            # if next_num not in visited:
            if not visited[int(next_num)]:
                # visited.add(next_num)
                visited[int(next_num)] = 1
                que.append((next_num, command + c))



t = int(input())
for _ in range(t):
    A, B = map(int, input().split())

    print(bfs(A, B))