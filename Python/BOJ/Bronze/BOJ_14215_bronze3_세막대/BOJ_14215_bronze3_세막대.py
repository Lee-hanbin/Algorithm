# BOJ_14215_bronze3_세막대
import sys
input = sys.stdin.readline

lst = sorted(list(map(int, input().split())), reverse=True)

if lst[0] < sum(lst[1:]):
    print(sum(lst))
else:
    print(sum(lst[1:])*2 -1)