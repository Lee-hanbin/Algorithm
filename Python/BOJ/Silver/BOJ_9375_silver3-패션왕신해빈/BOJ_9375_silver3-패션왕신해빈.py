# BOJ_9375_silver3-패션왕신해빈

from collections import defaultdict
import math
import sys
input = sys.stdin.readline

for i in range(int(input())):
    dict1 = defaultdict(int)
    sol = 0
    n = int(input())
    for i in range(n):
        x, y = input().split()
        if y not in dict1.keys():
            dict1[y] = 2
        else:
            dict1[y] += 1
    lst = list(dict1.values())
    sol = math.prod(lst)
    print(sol-1)