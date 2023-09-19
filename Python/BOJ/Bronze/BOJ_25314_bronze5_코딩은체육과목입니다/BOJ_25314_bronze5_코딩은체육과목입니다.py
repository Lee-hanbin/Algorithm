# BOJ_25314_bronze5_코딩은체육과목입니다

import sys
input = sys.stdin.readline

n = int(input())

s = ''

for i in range(n//4):
    s += 'long '
    
print(s + 'int')