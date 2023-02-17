# BOJ_9519_gold5-졸려

import sys

input = sys.stdin.readline


n = int(input())
s = input().strip()


length = len(s)

for i in range(n):
    
    if s == base:
        idx = i
        break
    left = ""
    right = "" 
    for j in range(1, length//2):
        if j % 2:   # 홀수번째
            left += s[length-1-j]
            left += s[j]
        else:       # 짝수번째
            right += s[length-1-j]
            right += s[j]
    else:
        base = left + right
else:
    print(base)
    exit()
    

for j in range(idx):
    left = ""
    right = "" 
    for j in range(1, length//2):
        if j % 2:   # 홀수번째
            left += s[length-1-j]
            left += s[j+1]
        else:       # 짝수번째
            right += s[length-1-j]
            right += s[j+1]
    else:
        base = left + right
else:
    print(base)
    exit()