# BOJ_5525_silver1-IOIOI

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

idx = 0
sol = 0
Pn = 'IOI'
Pn_cnt = 0

while idx < m-1:
    # 'IOI' 이면 1 'IOIOI' 이면 2 
    # => 기본 패턴인 'IOI'가 나오고 idx + 2 후에도 'IOI'이면 'IOIOI'를 뜻한다.
    if s[idx:idx+3] == Pn:
        Pn_cnt += 1
        if Pn_cnt == n:
            sol +=1
            Pn_cnt -= 1
        idx += 2
    
    # 만약 패턴이 깨지면 인덱스를 1만 늘려주고 패턴 카운트는 초기화
    else:
        Pn_cnt = 0
        idx += 1
         
print(sol)