# BOJ_7785_silver5_회사에 있는 사람
import sys
from collections import defaultdict
input =sys.stdin.readline

n = int(input())
box = defaultdict(int)
for _ in range(n):
    name, command = input().split()
    if command == 'enter':
        box[name] = 1
    else:
        box[name] = 0

sol = []
for k, v in box.items():
    if v:
        sol.append(k)

sol.sort(reverse=True)
for i in sol:
    print(i)

