# BOJ_14502_gold4-연구소

'''
어차피 완전 탐색해야지 방법없어
=> 0의 개수를 구해서 dictionary에 하나씩 담고
=> 해당 개수만큼 bit 연산자를 통해 경우의 수를 만들어
=> 해당 0 위치에 1씩 채워 넣고 0의 개수를 구하는 함수 만들어
'''

from copy import deepcopy
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]


# 바이러스를 모두 체크하고 안전지역의 수를 체크하는 함수
def bfs(lst_cmb):
    que = deque()
    # visited_set = deepcopy(virus_idx)
    # while visited_set:
        # v = visited_set.pop()
    for i in virus_lst:
        que.append(i)
        while que:
            r, c = que.popleft()
            for i in range(4):
                nr = dr[i] + r
                nc = dc[i] + c
                if 0<= nr <= n-1 and 0 <= nc <= m-1 and lst_cmb[nr][nc] == 0:
                    lst_cmb[nr][nc] = 2
                    que.append((nr,nc))
    chk = 0
    for i in lst_cmb:           
        chk += i.count(0)
    return chk

# 조합 구하는 함수
def nCr(n, r, s):
    global sol 
    if r == 0:
        after_lst = deepcopy(lst)       # deepcopy를 통해 처음 입력받은 map을 깊은복사
        for i in comb:                  # 조합을 통해 얻은 3개의 0을 1로 변경
            x, y = zero_dict[i]
            after_lst[x][y] = 1
        tmp =bfs(after_lst)             # 변경된 map을 bfs로 돌림
        if sol < tmp:                   # 최대값 구하기
            sol = tmp
    else:
        for i in range(s, n-r+1):
            comb[r-1] = lst_ncr[i]
            nCr(n, r-1, i+1)
########################################################################################
# main #

# 0: 빈칸
# 1: 벽
# 2: 바이러스

n, m = map(int, input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
zero_dict = defaultdict(tuple)

# virus_idx = set()
virus_lst = []

zero_cnt = 1
sol = 0
for i in range(n):
    for j in range(m):
        if lst[i][j] == 0:                  
            zero_dict[zero_cnt] = (i,j)    # 0의 순번을 key로 하고 좌표를 value로 하는 dictionary 정의
            zero_cnt += 1                  # 조합을 구하기 위해 zero의 개수도 카운팅
        elif lst[i][j] == 2:               # bfs를 위해 2가 위치하는 좌표를 담는다.
            # virus_idx.add((i,j))
            virus_lst.append((i,j))

# 빈칸을 3개 고르는 모든 경우의 수 구하기
lst_ncr = list(range(1,zero_cnt))
r = 3
comb = [0] * r
nCr(zero_cnt-1, r, 0)                     # 조합을 통해 빈칸 3개를 고르는 조합을 만들어서 bfs 실행
print(sol)