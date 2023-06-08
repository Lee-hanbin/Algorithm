# BOJ_20529_silver1-가장가까운세사람의심리적거리

import sys
from itertools import combinations

input = sys.stdin.readline

def operater(mbti:tuple):
    A, B = mbti
    cnt = 0
    for i in range(4):
        if A[i] != B[i]:
            cnt += 1
    return cnt



T = int(input())
sol = [1e12] * T

for i in range(T):
    n = int(input())
    lst = list(input().split())
    lst.sort()
    for people in combinations(lst[:16], 3):
        tmp = 0
        for mbti in combinations(people, 2):
            tmp += operater(mbti)
        sol[i] = min(sol[i], tmp)
        if not sol[i]:
            break

for i in sol:
    print(i)