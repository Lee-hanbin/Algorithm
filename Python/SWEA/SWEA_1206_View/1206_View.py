#SWEA 1206 View
import sys
sys.stdin = open('input.txt')

T = 10

for t in range(1,T+1):
    sol = 0
    n = int(input())
    building = list(map(int, input().split()))
    for i in range(2, n-2):
        before = max(building[i-2], building[i-1])      # 이전 빌딩
        after = max(building[i+1], building[i+2])       # 이후 빌딩
        target = building[i]                            # 현재 빌딩
        if before < target and after < target:          # 조망권 확보
            sol += target - max(before, after)          # 확보되면 세대수 체크

    print(f'#{t} {sol}')

# for test_case in range(1,11):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     cnt = 0
#     chk = 0
#     for i in range(2, N-2):
#         chk = lst[i]
#         case = []
#         for j in range(5):
#             if j == 2:
#                 case.append(0)
#             else:
#                 case.append(lst[i-2+j])
#         if case[0] < chk and case[1] < chk and case[3] < chk and case[4] < chk:
#             case.sort()
#             cnt += (chk-case[4])

#     print(f'#{test_case} {cnt}')
