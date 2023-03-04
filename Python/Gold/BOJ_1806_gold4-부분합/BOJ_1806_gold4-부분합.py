# BOJ_1806_gold4-부분합

import sys

input = sys.stdin.readline

n, s = map(int, input().split())

number_lst = list(map(int, input().split()))

cul_lst =  [0] * (n+1)
for i in range(1,n+1):
    cul_lst[i] = cul_lst[i-1] + number_lst[i-1]

sol = 100000
if cul_lst[-1] < s:
    print(0)
else:
    front, rear = 1, 1
    while front < n+1:
        if cul_lst[rear] - cul_lst[front-1] >= s:
            sol = min(sol, rear - front + 1)
            front += 1
        else:
            if rear < n:
                rear += 1
            else:
                break
    print(sol)