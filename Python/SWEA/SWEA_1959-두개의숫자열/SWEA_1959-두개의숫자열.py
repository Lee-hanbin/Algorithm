# SWEA_1959-두개의숫자열

from collections import deque

def operator(small_que, big_que, gap):
    sol = 0
    for _ in range(gap):
        chk = 0
        for i,e in enumerate(small_que):
            chk += e * big_que[i]
        if sol < chk:
            sol = chk
        big_que.rotate(-1)
    return sol

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    A = deque(map(int, input().split()))
    B = deque(map(int, input().split()))

    gap = abs(N - M) + 1
    if N < M:
        res =operator(A, B, gap)
    else:
        res = operator(B, A, gap)

    

    print(f'#{t} {res}')