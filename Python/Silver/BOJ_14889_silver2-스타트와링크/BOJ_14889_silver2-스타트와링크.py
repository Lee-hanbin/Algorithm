# BOJ_14889_silver2-스타트와링크

import sys
from itertools import combinations


input = sys.stdin.readline

n = int(input())

map1 = [list(map(int, input().split())) for _ in range(n)]

sol = 10 * 100

for i in combinations(list(range(n)), n//2):
    start_point = 0
    link_point = 0

    set_total = set(range(n))
    set_start = set(i)
    set_link = (set_total - set_start)
    
    # 스타트팀 능력치
    for r, c in combinations(i,2):
        start_point += map1[r][c] + map1[c][r]
    # 링크팀 능력치
    for r, c in combinations(list(set_link), 2):
        link_point += map1[r][c] + map1[c][r]
    # 두 팀의 능력치 차이
    sol = min(sol, abs( link_point - start_point))

print(sol)