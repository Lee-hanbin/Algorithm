# BOJ_19532_bronze2_수학은비대면강의입니다
import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

over = a*e-b*d
print((e*c-b*f)//over, (-c*d +a*f)//over)