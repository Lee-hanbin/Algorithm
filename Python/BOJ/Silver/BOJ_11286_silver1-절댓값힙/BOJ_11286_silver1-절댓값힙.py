# BOJ_11286_silver1-절댓값힙

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())

lst = []

for i in range(n):
    num = int(input())

    if num < 0:                 # 음의 정수이면
        num = abs(num) - 0.1    # 절대값에 0.1 빼기
        heappush(lst, num)
    elif num > 0:               # 자연수이면
        heappush(lst,num)       # 그대로 큐에 넣기
    else:                       # 0이 들어오면
        if len(lst):            # 큐에 요소가 있을때
            sol = heappop(lst)  # 최소값을 뽑고
            if type(sol) == int:    # 최소값이 정수이면
                print(sol)      # 출력
            else:               # 최소값이 소수이면
                sol += 0.1          # 0.1을 더해서
                print(-1*int(sol))  # 음의 정수로 출력
        else:                   # 큐가 비어있으면
            print(0)            # 0 출력


