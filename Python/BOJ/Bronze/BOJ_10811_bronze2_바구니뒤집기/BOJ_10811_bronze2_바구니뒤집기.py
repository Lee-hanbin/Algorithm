# BOJ_10811_bronze2_바구니뒤집기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ba = list(range(n+1))

for _ in range(m):
    l, r = map(int, input().split())

    # gap = r - l + 1

    tmp = ba[l:r+1][::-1]

    ba = ba[:l] + tmp + ba[r+1:]

print(*ba[1:])