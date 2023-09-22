# BOJ_1735_silver3_분수합
import sys
from math import lcm, gcd
input = sys.stdin.readline

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())


# 두 분모의 최소공배수 구하기
# chk1, chk2 = b1, b2
# while chk2:
#     tmp = chk1
#     chk1= chk2
#     chk2 = tmp%chk2

# self_lcm = b1*b2//chk1
self_lcm = lcm(b1, b2)
a = a1*(self_lcm//b1) + a2*(self_lcm//b2)
if (a -self_lcm) == 0:
    print(1, 1)
else:
    if gcd(a, self_lcm) > 1:
        sol_a =  a // gcd(a, self_lcm)
        sol_b = self_lcm// gcd(a, self_lcm)
        print(sol_a, sol_b)
    else:
        print(a,self_lcm)