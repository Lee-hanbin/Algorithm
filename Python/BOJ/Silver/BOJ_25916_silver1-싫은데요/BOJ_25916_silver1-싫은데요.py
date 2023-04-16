# BOJ_25916_silver1-싫은데요

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

jar = list(map(int, input().split()))
front, rear = 0, 0
sol = 0
chk = 0


while front < n:
    # print('front :', front)
    # print('rear  :', rear)
    # print('chk   :', chk)
    # print('sol   :', sol)
    # print()

    # front와 rear가 같은 경우
    if front == rear:
        chk = jar[front]
        rear += 1
    else:
        # 햄스터의 머리가 항아리 끝이 아닌경우
        if rear < n:
            if chk > m:             # 햄스터의 부피보다 큰 경우
                chk -= jar[front]
                front += 1
            else:                   # 햄스터의 부피보다 작은 경우
                chk += jar[rear]
                rear += 1
        # 햄스터의 머리가 항아리 끝인 경우 
        else:
            if chk > m:             # 햄스터의 부피보다 큰 경우는 햄스터를 줄임
                chk -= jar[front]
                front += 1
            else:                   # 햄스터의 부피보다 작은 경우, break
                break

    if chk <= m:
        sol = max(chk, sol)    

print(sol)