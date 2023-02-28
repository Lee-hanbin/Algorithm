# BOJ_25916_silver1-싫은데요

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

jar = list(map(int, input().split()))

que = deque()
que.append(jar.pop())
sol = 0
while que:
    # print(que)
    # print(jar)
    volume = sum(que)
    if volume < m:
        tmp = volume + jar[-1] if jar else volume

        if tmp < m:
            if jar:
                que.append(jar.pop()) 
            else:
                sol = max(sol, volume)
                break
        elif tmp > m:
            sol = max(sol, volume)
            que.popleft()
            que.append(jar.pop())
        else:
            sol = m
            break
    elif volume > m:
        que.popleft()
        if jar:
            que.append(jar.pop())
    else:
        sol = m
        break
print(sol)
    
# if jar.count(m) > 1:
#     print(m)
# else:
#     head, tail = 0, 1
#     sol = 0
#     while tail < n+2:
#         volume = sum(jar[head:tail])
#         if volume <= m:
#             tail += 1
#         else:
#             tmp = volume - jar[tail-1] 
#             if tmp <= m:
#                 sol = max(sol, tmp)
#             head += 1
#         # print('volume: ', volume)
#         # print('haed : ', head)
#         # print('tail : ', tail)
#         # print()
#         if head == tail and tail < n+1:
#             tail += 1
#     print(int(sol))