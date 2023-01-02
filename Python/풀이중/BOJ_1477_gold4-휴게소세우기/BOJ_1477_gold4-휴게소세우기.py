# BOJ_1477_gold4-휴게소세우기

import sys
input = sys.stdin.readline

n, m, L = map(int, input().split())
lst = [1] + list(map(int, input().split())) +[L]
lst.sort()
n = n+2
lst2 = []
for i in range(n-1):
    lst2.append(lst[i+1]- lst[i])

for _ in range(m):
    tmp = 0
    idx = 0
    # 최대 사이 거리 찾기
    for j, e in enumerate(lst2):
        if tmp < e:
            idx = j
            tmp = e
            print(tmp)
    plus = (lst[j-1] + lst[j-2])//2
    print(plus)
    lst.append(plus)
    lst.sort()
    n += 1
    lst2 = []
    for i in range(n-1):
        lst2.append(lst[i+1]- lst[i])
    print(lst2)
print(max(lst2))
    
