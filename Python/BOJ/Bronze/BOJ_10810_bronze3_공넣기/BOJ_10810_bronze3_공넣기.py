# BOJ_10810_bronze3_공넣기

import sys
input = sys.stdin.readline


# 도현이 바구니 n개
# 1~n 번호 공 많음
# 바구니에 공 하나씩만 넣을 수 있음
# m번 공을 넣으려고 함, 이미 있는 공은 빼고 새로운 공만 넣음
# m개의 (i, j, k) 가 존재할 때, i ~ j번 바구니에 k번 공을 넣을거임

n, m = map(int, input().split())

flag_lst = [0] * (n +1)

for _ in range(m):
    i, j, k = map(int, input().split())

    for l in range(i, j+1):
        flag_lst[l] = k


print(*flag_lst[1:])