# BOJ_2485_silver4-가로수
import sys
from math import gcd

input = sys.stdin.readline

n = int(input())

num = [int(input()) for _ in range(n)]
d = num[1] - num[0]
for i in range(1, n-1):
    d = gcd(d, num[i+1]-num[i])

cnt = 0
for i, e in enumerate(num):
    if i != len(num)-1:
        if e + d == num[i+1]:
            continue
        else:
            cnt += (num[i+1] - num[i] - d ) // d
            # tmp = e
            # while tmp + d != num[i+1]:
            #     cnt += 1
            #     tmp = tmp + d
print(cnt)