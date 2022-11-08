# BOJ_5430_gold5-AC

from collections import deque
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    que = deque()
    # 인풋 받기
    s = input().strip()
    n = int(input())
    operator = list(input().strip().rstrip(']').lstrip('[').split(','))    
    s = s.replace('RR','').strip()  # R이 연속으로 두번 나오면 그대로 이므로 제거
    length_D = s.count('D')         # D의 개수를 헤아려서 연산 전에 결과 값 도출
    switch = 0                      # R의 초기값 0
    if length_D > n:                # D 가 숫자보다 많으면 error
        print('error')
    elif length_D == n:             # D 가 숫자랑 같으면 []
        print('[]')
    else:                           # D 가 숫자보다 적으면 연산
        for i in operator:          # popleft 사용을 위해 deque에 넣기
            que.append(i)
        for i in s:                 # 연산 실행
            if i =='R':             
                if switch == 0:     # switch를 통해 R의 뒤집힘 여부를 체크
                    switch = 1
                else:
                    switch = 0
            else:                   
                if switch == 0:     # 연산이 정방향이면 popleft
                    que.popleft()
                else:               # 연산이 역방향이면 pop
                    que.pop()
        sol = '['
        if switch == 1:             # 연산이 역방향이면 pop
            while que:
                sol = sol + que.pop() +','
        else:                       # 연산이 정방향이면 popleft
            while que:  
                sol = sol + que.popleft() +','
        sol = sol.rstrip(',')+']'
        print(sol)