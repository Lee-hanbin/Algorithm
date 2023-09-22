# BOJ_2501_bronze3_약수구하기
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

for i in range(1, n+1):
    if not n%i:
        k -= 1
        if not k:
            print(i)
            break
else:
    print(0)