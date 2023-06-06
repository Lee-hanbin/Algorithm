# BOJ_18110_silver4-solved.ac

import sys

input = sys.stdin.readline


# round는 오사오입이기에 미세한 숫자를 더해주어 사사오입을 구현
def roundTraditional(val, digits):
    return int(round(val+10**(-len(str(val))-1), digits))

n = int(input())

if not n:
    print(0)
else:
    lst = list(int(input()) for _ in range(n))

    lst.sort()

    # exc = round(n * 0.15)
    exc = roundTraditional(n*0.15, 0)
    lst = lst[exc:n-exc]
    # n = 10 exc = 3 => lst[3:7] => 3, 4, 5, 6  ( 0, 1, 2 절삭, 7, 8, 9 절삭)
    sol = 0

    if lst:
        # sol = round(sum(lst)/len(lst))
        sol = roundTraditional(sum(lst)/len(lst), 0)

    print(sol)