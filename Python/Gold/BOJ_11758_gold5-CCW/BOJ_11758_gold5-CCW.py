import sys

input = sys.stdin.readline

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# 벡터 두 개 구하기
v_A = (x2-x1, y2-y1)
v_B = (x3-x2, y3-y2)

# 외적 구하기
cross_product = v_A[0]*v_B[1] - v_A[1]*v_B[0] 

# 0보다 크면 반시계
# 0보다 작으면 시계
# 0이면 수직선
if cross_product > 0:
    print(1)
elif cross_product == 0:
    print(0)
else:
    print(-1)