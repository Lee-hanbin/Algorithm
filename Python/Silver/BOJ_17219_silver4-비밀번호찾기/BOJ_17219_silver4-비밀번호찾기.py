# BOJ_17219_silver4-비밀번호찾기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memo_note = dict()
for i in range(n):
    s, p = input().split()
    memo_note[s] = p
for i in range(m):
    s = input().strip()
    print(memo_note[s])