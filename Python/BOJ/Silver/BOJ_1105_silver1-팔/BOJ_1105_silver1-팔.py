# BOJ_1105_silver1-팔

import sys

input = sys.stdin.readline

L, R = input().split()

cnt = 0

while len(L) != len(R):
    L = '0' + L

for i in range(len(L)):
    if L[i] == R[i]:
        if L[i] == '8':
            cnt += 1
    else:
        break

print(cnt)