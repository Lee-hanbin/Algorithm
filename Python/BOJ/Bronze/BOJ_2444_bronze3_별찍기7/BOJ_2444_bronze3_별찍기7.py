# BOJ_2444_bronze3_별찍기7
import sys
input = sys.stdin.readline


n = int(input())


for i in range(1, 2*n):
    if i < n:
        s = ' ' * (n - i)
        s += '*'* (2 * i - 1)
    else:
        s = ' ' * (i - n)
        s += '*'* (2 * (n-(i-n)) - 1)

    print(s)