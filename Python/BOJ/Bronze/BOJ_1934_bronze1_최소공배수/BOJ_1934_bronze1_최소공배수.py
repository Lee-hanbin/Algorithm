# BOJ_1934_bronze1_최소공배수
import sys
from math import gcd, lcm

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    l, r = map(int, input().split())
    print(lcm(l, r))