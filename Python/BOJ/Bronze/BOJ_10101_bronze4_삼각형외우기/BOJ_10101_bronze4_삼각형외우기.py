# BOJ_10101_bronze4_삼각형외우기
import sys
input = sys.stdin.readline

chk_lst = [int(input()) for _ in range(3)]
tmp = sum(chk_lst)


if tmp == 180:
    if chk_lst.count(60) == 3:
        print('Equilateral')
    elif (chk_lst.count(chk_lst[0])>1 or chk_lst.count(chk_lst[1])>1):
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')