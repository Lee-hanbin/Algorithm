# BOJ_15593_bronze2-Lifeguards

import sys

input = sys.stdin.readline

n = int(input())

lifeguards = [list(map(int, input().split())) for _ in range(n)]

# chk_lifeguards = lifeguards[::]

sol = 0

# while chk_lifeguards:
    # idx = chk_lifeguards.pop()
for idx in lifeguards:
    hire_lifeguards = [0] * 1001
    for s, e in lifeguards:
        if [s, e] == idx:
            continue
        for i in range(s+1, e+1):
            hire_lifeguards[i] = 1
    chk = sum(hire_lifeguards)
    if sol < chk:
        sol = chk 
        
print(sol)
    