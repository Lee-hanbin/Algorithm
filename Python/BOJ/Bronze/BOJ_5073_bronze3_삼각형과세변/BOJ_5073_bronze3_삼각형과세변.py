# BOJ_5073_bronze3_삼각형과세변
import sys
input = sys.stdin.readline

for lst in sys.stdin:
    lst = list(map(int, lst.split()))
    if not sum(lst):
        break
    lst.sort()
    if lst[2] >= sum(lst[:2]):
        print('Invalid')
    else:
        if lst.count(lst[0]) == 3:
            print('Equilateral')
        elif lst.count(lst[0]) > 1 or lst.count(lst[1]) > 1:
            print('Isosceles')
        else:
            print('Scalene') 