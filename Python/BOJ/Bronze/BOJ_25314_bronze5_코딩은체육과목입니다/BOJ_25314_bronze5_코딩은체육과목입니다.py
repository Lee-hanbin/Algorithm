import sys
input = sys.stdin.readline

n = int(input())

s = ''

for i in range(n//4):
    s += 'long '
    
print(s + 'int')