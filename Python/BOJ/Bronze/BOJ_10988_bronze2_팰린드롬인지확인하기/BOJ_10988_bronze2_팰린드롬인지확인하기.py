# BOJ_10988_bronze2_팰린드롬인지확인하기

import sys
input = sys.stdin.readline

s = input().rstrip()
length = len(s)
for i in range(length//2):
    if s[i] != s[length-i-1]:
       print(0)
       break
else:
    print(1)