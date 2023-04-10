# BOJ_2343_silver1-기타레슨

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

start = max(lst)
end = sum(lst)

while start <= end:
    mid = (start + end) // 2

    cnt = 1
    length = 0

    for chk in lst:
        if length + chk <= mid:
            length += chk
        else:
            length = chk
            cnt += 1
    
    if cnt <= m:
        end = mid - 1
    else:
        start = mid + 1

print(start)