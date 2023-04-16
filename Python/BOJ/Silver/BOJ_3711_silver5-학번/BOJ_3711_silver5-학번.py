# BOJ_3711_silver5-학번

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    G = int(input())
    student_num = list(int(input().rstrip()) for _ in range(G))
    sol = 1
    while 1:
        chk_set = set()
        # cnt = 0
        for i, num in enumerate(student_num):
            chk_set.add(num % sol)
            if len(chk_set) != i + 1:
                sol += 1
                break
        else:   
            break
    print(sol)