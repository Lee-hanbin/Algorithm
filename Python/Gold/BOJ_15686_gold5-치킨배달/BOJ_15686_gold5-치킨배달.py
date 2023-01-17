# BOJ_15686_gold5-치킨배달

import sys
from itertools import combinations


input = sys.stdin.readline

n, m = map(int, input().split())

map1 = []
lst_home = []
lst_chicken = []
sol = float('inf')

# 집과 치킨집의 인덱스를 체크
for i in range(n):
    map1.append(list(map(int,input().split())))
    for j, e in enumerate(map1[i]):
        if e == 1:
            lst_home.append((i, j))
        elif e == 2: 
            lst_chicken.append((i, j))

chicken_length = len(lst_home)

# 치킨집 중에 m개를 뽑아서 치킨거리 갱신
for idx in combinations(lst_chicken, m):
    chicken_load_lst = [float('inf')] * chicken_length
    idx = list(idx)
    while idx:
        r, c = idx.pop()
        for i, home_idx in enumerate(lst_home):
            chicken_load = abs(r-home_idx[0]) + abs(c-home_idx[1])
            if chicken_load_lst[i] > chicken_load:
                chicken_load_lst[i] = chicken_load
    chk = sum(chicken_load_lst)
    if sol > chk:        
        sol = chk

print(sol)