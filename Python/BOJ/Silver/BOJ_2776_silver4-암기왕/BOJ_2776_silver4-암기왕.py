# BOJ_2776_silver4-암기왕

import sys
input = sys.stdin.readline

T = int(input().strip())
for t in range(T):
    n1 = int(input().strip())
    set1 = set(map(int,input().split()))
    n2 = int(input().strip())
    for i in map(int,input().split()):
        if i in set1:
            print(1)
        else:
            print(0)