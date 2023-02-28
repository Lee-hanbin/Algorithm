# BOJ_25916_silver1-싫은데요

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

jar = list(map(int, input().split())) + [1e9, 1e9]


if jar.count(m) > 1:
    print(m)
else:
    head, tail = 0, 1
    sol = 0
    while tail < n+2:
        volume = sum(jar[head:tail])
        if volume <= m:
            tail += 1
        else:
            tmp = volume - jar[tail-1] 
            if tmp <= m:
                sol = max(sol, tmp)
            head += 1
        # print('volume: ', volume)
        # print('haed : ', head)
        # print('tail : ', tail)
        # print()
        if head == tail and tail < n+1:
            tail += 1
    print(int(sol))