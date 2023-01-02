# # BOJ_1074_silver1-Z

import sys
input = sys.stdin.readline

def func(num, idx, sol):
    global r, c, switch, rst
    if switch:            # 답을 찾으면 연산 그만
        return
    nr, nc = idx            # 현재 행과 열
    n_idx = 2**num          # 사각형의 추가 인덱스
    op = 2 ** ( 2 * num )   # 추가할 연산

    for i, e in enumerate([(nr,nc), (nr, nc + n_idx), (nr + n_idx, nc), (nr + n_idx, nc + n_idx)]): # 작은 사각형 시작할 인덱스
        n_sol = sol + (op * i)
        if (r,c) == e:          # 답을 찾으면 switch on
            rst = n_sol         # 답을 할당
            switch = True       
            return
        if num > 0 and e[0] <= r < e[0] + n_idx and e[1] <= c < e[1] + n_idx:  # 찾는 인덱스가 사각형 안에 있을 경우에만 재귀함수
            func(num -1, e, n_sol)

n, r, c = map(int,input().split())
switch, rst = False, 0
func(n, (0, 0), 0)
print(rst)