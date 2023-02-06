# BOJ_2166_gold5-다각형의면적

import sys

input = sys.stdin.readline

N = int(input())

points = [list(map(int, input().split())) for _ in range(N)]

points = points + [points[0]]

up = 0
down = 0

for i in range(N):
    up += (points[i][0] * points[i+1][1])
    down += (points[i][1] * points[i+1][0])
    
sol =  abs(up - down) * 0.5

print(round(sol,1))



# # 틀린 풀이... 오목한 다각형 고려 x

# import sys

# input = sys.stdin.readline

# def triangle_S(lst):
#     x1, y1 = fixed_point
#     x2, y2 = lst[0]
#     x3, y3 = lst[1]
#     return 0.5*abs(x1*y2 + x2*y3 + x3*y1 - x1*y3 - x3*y2 - x2*y1)

# N = int(input())

# points = [list(map(float, input().split())) for _ in range(N)]

# fixed_point = points[0]


# sol = 0
# for i in range(1, N-1):
#     sol += triangle_S(points[i:i+2])

# print(round(sol,1))