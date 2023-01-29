# BOJ_1106_gold5-호텔

import sys

input = sys.stdin.readline

C, N = map(int, input().split())                                        # C(k) :  고객 , N(n) : 도시  

table = [float('inf')] * (C+ 100)

lst = [list(map(int, input().split())) for _ in range(N)]

lst_sort = sorted(lst, key=lambda x: x[0])

table[0] = 0

for cost, customer in lst_sort:
    # if customer > C:
    #     continue
    for j in range(customer, C+100):
        # if j + customer <= C and table[j] != float('inf'):
        table[j] = min(table[j-customer]  + cost, table[j] )
        # if j >= C:
            # table[customer] = min(table[customer], cost)
print(min(table[C:]))