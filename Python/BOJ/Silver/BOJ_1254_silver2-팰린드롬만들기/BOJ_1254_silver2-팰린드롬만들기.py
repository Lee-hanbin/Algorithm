# BOJ_1254_silver2-팰린드롬만들기

import sys

input = sys.stdin.readline

def pd(s):
    if s == s[::-1]:
        return True
    else:
        return False

s = input().rstrip()
length = len(s)

if pd(s):
    print(len(s))
else:
    for i in range(1, length + 1):
        if pd(s + s[:i][::-1]):
            print(length + i)
            break
    
