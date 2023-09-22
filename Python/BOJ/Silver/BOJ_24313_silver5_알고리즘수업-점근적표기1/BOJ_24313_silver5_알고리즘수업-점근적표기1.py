# BOJ_24313_silver5_알고리즘수업-점근적표기1
import sys
input = sys.stdin.readline  

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

f = a0
g = (c-a1) * n0

if f <= g and a1 <= c:
    print(1)
else:
    print(0)