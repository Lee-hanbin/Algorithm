# BOJ_16507_silver1-어두운건무서워

import sys

input = sys.stdin.readline

r, c, q = map(int, input().split())

num_lst = [[0] *(c+1)] + list([0] + list(map(int, input().split())) for _ in range(r))


for i in range(1, r+1):
    for j in range(1, c+1):
        num_lst[i][j] = num_lst[i-1][j] + num_lst[i][j-1] + num_lst[i][j] - num_lst[i-1][j-1]

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    size = (r2- r1 + 1) * (c2-c1+1)
    print((num_lst[r2][c2] - num_lst[r1-1][c2] - num_lst[r2][c1-1] + num_lst[r1-1][c1-1])//size)

