# BOJ_12015_gold2-가장긴증가하는부분수열2

import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
seq = [lst[0]]
ans = 1

for num in lst[1:]:
    
    # 수열의 끝 값과 비교해서 더 크면 담는다
    if seq[-1] < num:
        seq.append(num)
        ans += 1
    # 수열의 끝 값과 비교해서 더 작거나 같으면 seq안에서 num보다 큰 수 중에 가장 작은 수를 찾아서 바꾼다
    else:
        index = bisect_left(seq, num)
        seq[index] = num

print(ans)