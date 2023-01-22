# BOJ_5635_silver5-생일

import sys

input = sys.stdin.readline

n = int(input())

db = [0] * n

for i in range(n):
    name, d, m, y = input().split()
    db[i] = [int(y), int(m), int(d), name]

db.sort(key= lambda x : (x[0], x[1], x[2]))


print(db[-1][3])
print(db[0][3])