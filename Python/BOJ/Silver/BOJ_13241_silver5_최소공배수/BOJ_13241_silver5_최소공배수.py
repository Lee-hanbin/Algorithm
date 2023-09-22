# BOJ_13241_silver5_최소공배수
import sys
from math import lcm
input = sys.stdin.readline

l, r = map(int,input().split())

# def Euclidean(a, b):
#     tmp = a % b;
#     if not tmp:
#         return b
#     return Euclidean(b, tmp)

# self_gcd = Euclidean(l, r)
# print(l*r//self_gcd)

a, b = l, r
while b:
    tmp = a
    a = b
    b = tmp % b

print(l*r//a)

# print(lcm(l, r))