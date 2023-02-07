# BOJ_2607_silver2-오락실에간총총이

import sys
input = sys.stdin.readline

n = int(input())

lst_row = []
lst_col = []

# Gom의 인덱스를 모두 리스트에 담는다.
for i in range(n):
    monitor = input().rstrip()
    for j, e in enumerate(monitor):
        if e == "G":
            lst_row.append(i)
            lst_col.append(j)

# 인덱스를 정렬한다.
lst_row.sort()
lst_col.sort()

# 최소값과 최대값을 뽑는다.
max_row, min_row = lst_row[-1], lst_row[0]
max_col, min_col = lst_col[-1], lst_col[0]

# 최소 최대 인덱스가 모두 같으면 0
if min_row == max_row and min_col == max_col:
    print(0)
# 한 row에 모든 곰이 있는 경우
elif min_row == max_row and min_col != max_col:
    print(min(max_col , (n-1)-min_col))
# 한 col에 모든 곰이 있는 경우
elif min_col == max_col and min_row != max_row:
    print(min(max_row , (n-1)-min_row))
# 나머지
else:
    case_1 = max_row + max_col
    case_2 = max_row + (n-1) - min_col
    case_3 = (n-1) - min_row + max_col
    case_4 = (n-1) - min_row + (n-1) - min_col

    print(min(case_1, case_2, case_3, case_4))