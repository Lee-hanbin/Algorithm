# BOJ_2313_gold5-보석구매하기

import sys
input = sys.stdin.readline

n = int(input())

sol = []
for _ in range(n):

    jewelry = int(input())
    jewelry_lst = list(map(int, input().split()))
    minsum_idx = [-1e12, 0, 0]
    tmp = 0
    start, end = 0, 0
    while end < jewelry:
        current = jewelry_lst[end]
        tmp += current

        if tmp <= current:
            start = end
            tmp = current

        if tmp > minsum_idx[0]:
            minsum_idx = [tmp, start+1, end+1]
        elif tmp == minsum_idx[0]:
            if (minsum_idx[2]- minsum_idx[1]) > end - start + 1:
                minsum_idx[1:] = [start+1, end+1]
        end += 1
    
    sol.append(minsum_idx)


# 각 줄의 보석 최대 가치 더하기
final_sum = sum(map(lambda x: x[0], sol))

print(final_sum)
for i in sol:
    print(*i[1:])
