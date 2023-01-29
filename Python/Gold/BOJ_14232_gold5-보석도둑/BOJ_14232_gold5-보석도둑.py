# BOJ_14232_gold5-보석도둑

import sys

input = sys.stdin.readline

num = int(input().rstrip())

c = 2
cnt = 0
lst = []

while num != 1:
    if c>=1000000:
        lst.append(num)
        cnt += 1
        break
    if not num % c:
        num //= c
        cnt += 1
        lst.append(c)
    else:
        c += 1

print(cnt)
print(*lst)
