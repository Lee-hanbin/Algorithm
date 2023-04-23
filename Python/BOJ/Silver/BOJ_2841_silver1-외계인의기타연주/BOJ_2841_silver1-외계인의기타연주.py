# BOJ_2841_silver1-외계인의기타연주

import sys
from collections import defaultdict

input = sys.stdin.readline

n, p = map(int, input().split())

sol = 0
check_dict = defaultdict(list)
for _ in range(n):
    line, flet = map(int, input().split())

    # 이미 누른적이 있는 줄
    if check_dict[line]:
        tmp = check_dict[line][::-1]
        # 프렛을 하나씩 확인
        for i in tmp:
            # 현재 프렛보다 크면 counting 후, 손가락 떼기
            if i > flet:
                sol += 1
                check_dict[line].pop()
            # 현재 프렛과 같으면 pass
            elif i == flet:
                break
            # 현재 프렛보다 작으면 counting 후, 프렛을 잡기
            else:
                sol += 1
                check_dict[line].append(flet)
                break
        # 손가락을 전부 다 떼면, 프렛을 잡고 counting
        else:
            sol += 1
            check_dict[line].append(flet)
    # 처음 누른 줄
    else:
        check_dict[line].append(flet)
        sol += 1
print(sol)