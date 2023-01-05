# BOJ_2887_Platinum5-행성터널

import sys
from collections import defaultdict

input = sys.stdin.readline


n = int(input())

idx_lst = [list(map, int(input().split())) for _ in range(n)]
graph = defaultdict(list)

for i in range(n):
    for j in range(i+1, n):

        
        