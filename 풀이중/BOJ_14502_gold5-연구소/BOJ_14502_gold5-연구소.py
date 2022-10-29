# BOJ_14502_gold5-연구소

'''
어차피 완전 탐색해야지 방법없어
=> 0의 개수를 구해서 dictionary에 하나씩 담고
=> 해당 개수만큼 bit 연산자를 통해 경우의 수를 만들어
=> 해당 0 위치에 1씩 채워 넣고 0의 개수를 구하는 함수 만들어
'''

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]




def bfs(lst):
    que = deque()
    while zero_idx:
        v = zero_idx.pop()
        que.append(v)
        while que:
            r, c = que.popleft()
            for i in range(4):
                nr = dr[i] + r
                nc = dc[i] + c
                # 0인 곳을 탐색하는데 해당 탐색 위치의 

# 조합 구하는 함수
def nCr(n, r, s):
    if r == 0:
        bfs(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = lst_ncr[i]
            nCr(n, r-1, i+1)

n, m = map(int, input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
zero_dict = defaultdict(list)


# 0: 빈칸
# 1: 벽
# 2: 바이러스

# zero_idx = set()

# 빈칸인 모든 좌표 구하기
cnt = 0
for i in range(n):
    for j in range(m):
        if lst[i][j] == 0:
            zero_dict[cnt].append((i,j))
            cnt += 1
            # zero_idx.add((i,j))
zero_cnt = cnt

# 빈칸을 3개 고르는 모든 경우의 수 구하기
lst_ncr = list(range(1,zero_cnt))
r = 3
comb = [0] * r
nCr(zero_cnt-1, r, 0)

# bfs()