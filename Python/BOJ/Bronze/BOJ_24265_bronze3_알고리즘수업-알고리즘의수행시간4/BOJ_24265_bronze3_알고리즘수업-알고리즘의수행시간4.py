# BOJ_24265_bronze3_알고리즘수업-알고리즘의수행시간4
import sys
input = sys.stdin.readline

n = int(input())
sol = 0
for i in range(1, n):
    sol += i
print(sol)
print(2)