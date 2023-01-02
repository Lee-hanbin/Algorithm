# BOJ_18428_gold5-감시피하기

import sys 
from collections import defaultdict
from copy import deepcopy

input = sys.stdin.readline

dr = [-1, 1, 0 ,0]
dc = [ 0, 0,-1, 1]

# 감시망을 확인하는 함수
def search(lst):
    def checking_func():

        for r,c in chk_teacher:                     # 선생님 위치를 모두 체크        
            for i in range(4):                      # delta search 
                nr = dr[i] + r
                nc = dc[i] + c
                while 0 <= nr < n and 0 <= nc < n:  # 복도 내에서 반복문
                    if lst[nr][nc] == 'S':          # 학생을 만나면 실패
                        return False
                    elif lst[nr][nc] == 'T' or lst[nr][nc] == 'O':  # 선생님이나 장애물을 만나면 다른 방향 탐색
                        break
                    nr = dr[i] + nr                 # 빈 공간이면 다음 칸으로 이동
                    nc = dc[i] + nc
        else:                                       # 학생을 찾을 수 없다면 True 반환
            return True
    return checking_func()

# 빈 공간 중에 3개를 고르는 조합함수
def nCr(n, r, s):
    global switch
    if r == 0:
        if switch == 1:             # 이미 True가 나왔으면 Pass
            return
        new_alias = deepcopy(alias) # 장애물 위치를 설치할 새로운 alias 정의
        for i in comb:              # 장애물의 위치를 체킹
            rr, cc = chk_blank[i]
            new_alias[rr][cc] = 'O'
        if search(new_alias):       # 감시에 성공하면 switch에 1 할당
            switch = 1
    else:
        for i in range(s, n-r+1):
            comb[r-1] = ncr_list[i]
            nCr(n, r-1, i+1)

#######################################################################
# main #

n = int(input().rstrip())

alias = [list(input().split()) for _ in range(n)]
chk_blank = defaultdict(tuple)
chk_teacher = []
switch = 0


# X의 idx와 좌표 체크 및 선생님 좌표 체크
idx = 1
for i in range(n):
    for j in range(n):
        if alias[i][j] == 'X':
            chk_blank[idx] = (i, j)
            idx += 1
        elif alias[i][j] == 'T':
            chk_teacher.append((i,j))

nCr_total = idx-1

# 조합생성
ncr_list = list(range(1,idx))
r = 3
comb = [0] * r 
nCr(nCr_total, r, 0)
if switch == 1:
    print('YES')
else:
    print('NO')
