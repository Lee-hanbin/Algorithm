# BOJ_2903_bronze3_중앙이동알고리즘
import sys
input = sys.stdin.readline

n = int(input())
# n1 = 3
# n2 = 5
# n3 = 9
# nm = nm-1 + 2**(m)

tmp = 2
sol = 0
for i in range(n):
    tmp += 2**(i)
    sol = tmp ** 2
    
print(sol)