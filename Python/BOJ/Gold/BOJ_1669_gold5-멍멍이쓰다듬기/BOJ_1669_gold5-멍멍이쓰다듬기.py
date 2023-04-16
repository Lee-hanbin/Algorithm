# BOJ_1669_gold5-멍멍이쓰다듬기

import sys

a, b = map(int, sys.stdin.readline().split())
if a == b:
    print(0)
else:
    n = int((b - a) ** 0.5)
    if n ** 2 == b - a:
        print(2 * n - 1)
    else:
        z = (b - a) - n ** 2
        if z <= n:
            print(2 * n)
        else:
            print(2 * n + 1)
# import sys

# from collections import deque



# def bfs(monkey, dog):
#     que = deque()
#     visited = set()
#     for i in [monkey-1, monkey, monkey+1]:
#         que.append([i, 2])
#         visited.add(i)
#     while que:
#         k, cnt = que.popleft()
#         for i in [1, 0, -1]:
#             if i + k not in visited and i + k > 0:
#                 visited.add(i + k)
#                 que.append([i+k, cnt + 1])
#                 if i+k == dog:
#                     return cnt + 1

# monkey, dog = map(int, input().split())

# chk = dog - monkey
# if chk == 0:
#     cnt = 0
# elif chk == 1:
#     cnt = 1
# elif chk == 2:
#     cnt = 2
# else:
#     cnt = 2
#     dog -= 1
#     monkey += 1
#     cnt += bfs(monkey, dog)
# print(cnt)
