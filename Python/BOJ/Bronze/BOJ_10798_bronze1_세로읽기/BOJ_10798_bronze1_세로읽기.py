# BOJ_10798_bronze1_세로읽기
import sys
input = sys.stdin.readline

s_lst = []
M_len = 0
sol = ''

for _ in range(5):
    s = input().rstrip()
    s_lst.append(s)
    M_len= max(len(s), M_len)

for i in range(M_len):
    for j in range(5):
        if i >= len(s_lst[j]):
            continue
        sol += s_lst[j][i]


print(sol)