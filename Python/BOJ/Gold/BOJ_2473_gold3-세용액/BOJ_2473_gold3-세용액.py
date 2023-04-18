# BOJ_2473_gold3-세용액

import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

lst.sort()

# 모두 양수
if lst[0] >= 0:
    print(lst[0],lst[1],lst[2])
# 모두 음수  
elif lst[-1] <= 0:
    print(lst[-3],lst[-2],lst[-1])
else:
    result = 1e12
    sol = []
    for i in range(n-2):
        left = i + 1
        right = n - 1
        
        while left < right:
            mix = lst[i] + lst[left] + lst[right]
            
            if abs(mix) < result:
                result = abs(mix)
                sol = [lst[i], lst[left], lst[right]]
            if mix < 0:
                left += 1
            elif mix > 0:
                right -= 1
            else:
                break
    print(*sol)