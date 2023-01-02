# 고정점 찾기

import bisect

def binary_search(s, e):
    if s > e:
        return -1
    mid = (s+e)//2
    if lst[mid] == mid:
        return mid
    elif lst[mid] > mid:        # 값이 인덱스보다 크면 왼쪽
        return binary_search(s, mid-1)
    else:                       # 값이 인덱스보다 작으면 오른쪽
        return binary_search(mid+1, e)

N = int(input())
lst = list(map(int, input().split()))

print(binary_search(0,N-1))
# for i in range(N):
#     if lst[i] == bisect.bisect_left(lst,lst[i]):
#         print(i)
#         break
#     # print(bisect.bisect_right(lst,lst[i]))
# else:
#     print(-1)


'''
5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 16

7
-15 -4 3 8 9 13 15
'''