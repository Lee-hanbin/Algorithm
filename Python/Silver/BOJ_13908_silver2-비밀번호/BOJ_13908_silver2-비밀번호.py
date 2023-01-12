# BOJ_13908_silver2-비밀번호

import sys
from itertools import combinations

n, m = map(int, input().split())


for i in range(m):
    lst = list(map(int, input().split()))

if n == m:
    print(len(combinations(lst, n)))
else:
    for i in range(9):
        if i not in lst:
            lst.append(i)
set1 = set(lst)
