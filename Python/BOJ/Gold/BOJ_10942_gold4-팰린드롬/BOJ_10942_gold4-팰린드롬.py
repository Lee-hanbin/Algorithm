# BOJ_10942_gold4-팰린드롬


#1. 투포인트.. 어림없지
# import sys

# input = sys.stdin.readline

# n = int(input())

# lst = list(map(int, input().split()))

# m = int(input())

# for i in range(m):
#     s, e = map(int, input().split())
#     length = e - s + 1
#     check_lst = lst[s-1:e]
#     for i in range(length//2):
#         if check_lst[i] == check_lst[-i-1]:
#             continue
#         else:
#             print(0)
#             break
#     else:
#         print(1)

#2. 디피..
import sys
input = sys.stdin.readline
n = int(input())
dp = [[0] * n for i in range(n)]
s = list(map(int, input().split()))
for b in range(n):
    for start in range(n):
        end = start + b
        if end >= n:
            break
        if start == end:
            dp[start][end] = 1
            continue
        if start + 1 == end:
            if s[start] == s[end]:
                dp[start][end] = 1
                continue
        if s[start] == s[end] and dp[start + 1][end - 1]:
            dp[start][end] = 1
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    print(dp[a - 1][b - 1])