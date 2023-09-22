# BOJ_24267_bronze2_알고리즘수업-알고리즘의수행시간6
import sys
input = sys.stdin.readline

n = int(input())
sol = 0
for i in range(1, n-1):
    j = n-1-i
    sol += (n-j-1)* j

print(sol)
print(3)

