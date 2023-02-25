# SWEA_5356_의석이의세로로말해요

import sys

sys.stdin = open('sample_input.txt')

for t in range(1, int(input())+1):
    lst = []
    max_len = 0

    # 단어 5개씩 입력받으면서 최장길이 갱신
    for i in range(5):
        lst.append(list(input().rstrip()))
        max_len = max(max_len, len(lst[i]))

    # 최장 길이만큼 리스트의 길이
    for i,e in enumerate(lst):
        chk = max_len - len(e)
        for _ in range(chk):
            lst[i].append("")

    # 가로세로 뒤집기
    sol = []
    for i in zip(*lst):
        sol.append(list(i))
    
    # 출력
    print(f'#{t} ',end="")
    for i in sol:
        for e in i:
            if e != '':
                print(e, end="")
    print()