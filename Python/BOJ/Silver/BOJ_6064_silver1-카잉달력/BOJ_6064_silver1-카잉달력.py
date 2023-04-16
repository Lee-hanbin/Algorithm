# BOJ_6064_silver1-카잉달력

import sys
from math import lcm
from collections import deque
input = sys.stdin.readline


# 1. 정수론 이용 풀이
def num(m, n, x, y):
    length = lcm(m, n)
    while x <= length:
        if (x-y) % n == 0:
            return x
        x += M
    return -1

t = int(input())
for _ in range(t):
    M, N, x, y = map(int, input().split())
    print(num(M, N, x, y))

# # 2. deque rotate 풀이
# t = int(input())
# for _ in range(t):
# M, N, x, y = map(int, input().split())
# M_que = deque(range(1,M+1))
# N_que = deque(range(1,N+1))
# length = lcm(M, N)
# for i in range(2,length):
#     M_que.rotate(-1)
#     N_que.rotate(-1)
#     # print(M_que)
#     # print(N_que)
#     if M_que[0] == x and N_que[0] == y:
#         print(i)
#         break
# else:
#     print(-1)

# # 3. 단순 구현 풀이
# t = int(input())
# for _ in range(t):
# M, N, x, y = map(int, input().split())
# start_x, start_y = 1, 1
# length = lcm(M, N)

# for i in range(2, length+1):
#     if start_x < M:
#         start_x += 1
#     else:
#         start_x = 1
#     if start_y < N:
#         start_y += 1
#     else:
#         start_y = 1

#     if start_x == x and start_y == y:
#         print(i)
#         break
# else:
#     print(-1)

