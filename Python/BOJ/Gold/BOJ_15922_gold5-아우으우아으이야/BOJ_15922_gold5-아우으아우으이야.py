# BOJ_15922_gold5-아우으우아으이야!!

import sys

input = sys.stdin.readline

n = int(input())

lst = [[0,0] for _ in range(n)]

flag = 0

x, y = map(int, input().split())
lst[flag] = [x, y]

for i in range(n-1):
    x, y = map(int, input().split())

    if x > lst[flag][1]:        # 선분이 중복되지 않는 경우.
        flag += 1
        lst[flag] = [x, y]  
    elif lst[flag][1] <= y:     # 선분이 중복되면서 길어지는 경우
        lst[flag][1] = y

sol = 0
for x, y in lst:
    sol += (y-x)

print(sol)