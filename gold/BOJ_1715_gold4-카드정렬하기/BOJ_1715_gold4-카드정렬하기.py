# BOJ_1715_gold4-카드정렬하기

import sys
input = sys.stdin.readline
from heapq import heappush, heapify, heappop

n = int(input())
lst = [0] * n
if n == 1:                  # 값이 하나면 비교할 수 없음 => 0 출력
    print(0)
    exit()
for i in range(n):
    lst[i] = int(input())
heapify(lst)                # 리스트를 heapq 에 넣는다.
sol = 0                     
while len(lst) > 1:         # lst의 값이 하나 남으면 비교 불가함
    a = heappop(lst)        # 첫번째 값
    b = heappop(lst)        # 두번째 값
    sol += a+b              # 누적합
    heappush(lst, a+b)      # 첫번째 + 두번째 를 다시 heapq에 넣기
print(sol)              
