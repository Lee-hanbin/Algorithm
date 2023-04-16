# BOJ_17144_gold4-미세머지안녕

import sys
from copy import deepcopy

input = sys.stdin.readline

def make_up_cycle(rr, cc):
    cycle = []
    cnt = 0
    switch = 0
    while not switch or (rr, cc) != up:
        if cnt == 0:
            cc += 1
            if cc == c:
                switch = 1
                rr -= 1
                cc -= 1
                cnt += 1
            cycle.append((rr, cc))
        elif cnt == 1:
            rr -= 1
            if rr == -1:
                rr += 1
                cc -= 1
                cnt += 1
            cycle.append((rr, cc))
        elif cnt == 2:
            cc -= 1
            if cc == -1:
                cc += 1
                rr += 1
                cnt += 1
            cycle.append((rr, cc))
        else:
            rr += 1
            if rr == up[0] + 1:
                rr -= 1
                cc += 1
                cnt = 0
            cycle.append((rr, cc))
    return cycle

def make_down_cycle(rr, cc):
    cycle = []
    cnt = 0
    switch = 0
    while not switch or (rr, cc) != down:
        if cnt == 0:
            cc += 1
            if cc == c:
                switch = 1
                rr += 1
                cc -= 1
                cnt += 1
            cycle.append((rr, cc))
        elif cnt == 1:
            rr += 1
            if rr == r:
                rr -= 1
                cc -= 1
                cnt += 1
            cycle.append((rr, cc))
        elif cnt == 2:
            cc -= 1
            if cc == -1:
                cc += 1
                rr -= 1
                cnt += 1
            cycle.append((rr, cc))
        else:
            rr -= 1
            if rr == down[0] - 1:
                rr += 1
                cc += 1
                cnt = 0
            cycle.append((rr, cc))
    return cycle


r, c, t = map(int, input().split())

map1 = []

up =  0
down = 0

dust_idx = set()

for i in range(r):
    map1.append(list(map(int, input().split())))
    for j, e in enumerate(map1[i]):
        if e == -1:
            if not up:
                up = (i, j)
            else:
                down = (i, j)
        elif e:
            dust_idx.add((i,j))

up_cycle = []
down_cycle = []

up_cycle = make_up_cycle(up[0], up[1])
down_cycle = make_down_cycle(down[0], down[1])


dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]


for i in range(t):
    tmp_lst = [[0]* c for _ in range(r)]

    while dust_idx:
        rr, cc = dust_idx.pop()
        value = map1[rr][cc] // 5
        chk = 0
        tmp_lst[rr][cc] += map1[rr][cc]
        if value > 0:
            for i in range(4):
                nr = dr[i] + rr
                nc = dc[i] + cc
                if 0 <= nr < r and 0 <= nc < c and (nr, nc) not in {up, down}:
                    tmp_lst[nr][nc] += value
                    chk += value
            tmp_lst[rr][cc] -= chk

    for cycle in [up_cycle, down_cycle]:
        for idx, (rr, cc) in enumerate(cycle):
            if not idx:
                tmp1 = tmp_lst[rr][cc]
                tmp_lst[rr][cc] = 0
                continue
            tmp2 = tmp_lst[rr][cc]
            tmp_lst[rr][cc] = tmp1
            tmp1 = tmp2
    
    tmp_lst[up[0]][up[1]] = -1
    tmp_lst[down[0]][down[1]] = -1

    map1 = deepcopy(tmp_lst)

    for i in range(r):
        for j in range(c):
            if map1[i][j] > 0:
                dust_idx.add((i, j))

sol = 2
for i in map1:
    sol += sum(i)

print(sol)