# BOJ_5397_silver2-키로거

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    password = input()
    l, r = [], []

    for i in password:
        if i == '-':
            if l:
                l.pop()
        elif i == '<':
            if l:
                r.append(l.pop())
        elif i == '>':
            if r:
                l.append(r.pop())
        else:
            l.append(i)
    
    l = l + r[::-1]
    print(''.join(l))