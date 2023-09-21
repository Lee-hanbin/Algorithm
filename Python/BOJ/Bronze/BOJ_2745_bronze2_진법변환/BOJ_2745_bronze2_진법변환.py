# BOJ_2745_bronze2_진법변환
import sys
input = sys.stdin.readline

n, b = input().split()

n = list(n)[::-1]
sol = 0

for i, e in enumerate(n):
    if ord(e) > 64:
        e = ord(e) - 55
    sol += (int(e) * int(b)**i)

print(sol)


# n,b=input().split()
# print(int(n,int(b)))