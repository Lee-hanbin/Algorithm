# BOJ_9063_bronze3_대지
import sys
input = sys.stdin.readline

n = int(input())
if n < 2:
    print(0)
else:
    l_sol = [10000, -10000]
    h_sol = [10000, -10000]
    for _ in range(n):
        l, h = map(int, input().split())
        l_sol = [min(l_sol[0], l), max(l_sol[1], l)]
        h_sol = [min(h_sol[0], h), max(h_sol[1], h)]
    print(abs(l_sol[1]-l_sol[0]) * abs(h_sol[1]-h_sol[0]))