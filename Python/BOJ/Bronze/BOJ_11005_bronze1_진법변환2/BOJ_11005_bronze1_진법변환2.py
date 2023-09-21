# BOJ_11005_bronze1_진법변환2
import sys
input = sys.stdin.readline

n, b = map(int, input().split())
sol = ''
di = 1
tmp = n
while n:
    tmp = n%b
    if tmp > 9:
        if tmp:
            tmp = chr( tmp + 55)
        else:
            tmp = chr( tmp + 55 + b)
    sol += str(tmp)
    n = n//b

print(sol[::-1])