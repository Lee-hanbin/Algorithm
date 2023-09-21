# BOJ_2720_bronze3_세탁소사장동혁
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    change = int(input())

    sol = []
    for i in [25, 10, 5, 1]:
        tmp = change//i
        sol.append(tmp)
        change -= i*tmp
    
    print(*sol)