# BOJ_10813_bronze2_공바꾸기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ba = list(range(n+1))

for _ in range(m):
    l, r = map(int, input().split())

    ba[l], ba[r] = ba[r], ba[l]


print(*ba[1:])