# BOJ_27231_gold5-2023년이기대되는이유

import sys
from itertools import combinations

input = sys.stdin.readline

for _ in range(int(input())):
    n = list(input().rstrip())

    # n이 0과 1로 이루어진 경우, 무수히 많음
    for i in n:
        if int(i) > 1:
            break
    else:
        print('Hello, BOJ 2023!')
        continue
    
    # 초기값을 data에 넣는다.
    chk = ""
    for num in n:
        chk += num
    chk = int(chk)
    data_set = set()
    data_set.add(chk)

    length = len(n)
    chk_num = list(range(1, length))

    # 더하기를 하나씩 늘리면서 모든 합을 data set에 담는다.
    for i in range(1, length):
        for idx in combinations(chk_num, i):
            dum = 0
            for k in range(i + 1):
                chk = ""
                if k == 0:
                    for num in n[:idx[0]]:
                        chk += num
                elif k == i:
                    for num in n[idx[-1]:]:
                        chk += num
                else:
                    for num in n[idx[k-1]:idx[k]]:
                        chk += num
                dum += int(chk)
            data_set.add(dum)

    # 각 자릿수의 제곱을 해서 더한값이 data set에 있으면 sol set에 넣기
    # 합이 data set에 있는 최대값보다 크면 break
    m = 0
    sol = 0
    sol_set = set()
    while 1:
        chk = 0
        for num in n:
            chk += int(num)**m
        if chk > max(data_set):
            break
        if chk in data_set:
            sol_set.add(chk)
        m += 1


    print(len(sol_set))