# BOJ_2342_gold3-dancedanceRevolution
import sys

input = sys.stdin.readline

# 1. dfs풀이(시간초과)
# sys.setrecursionlimit(10**6)

# def dfs(foot_move:list, idx:int, power:int):
#     global sol
#     current_number = sequence[idx]
#     # sol보다 더 커지면 스탑
#     if sol < power:
#         return

#     # 수열이 끝까지 가면 갱신
#     if not current_number:
#         sol = power
#         return

    
#     if current_number in foot_move:     #이미 foot_move에 발을 대고 있으면
#         dfs(foot_move, idx+1, power + 1)
#     else:
#         if not foot_move[0]:            #왼발이 아직 가운데 있으면
#             dfs([current_number, foot_move[1]], idx+1, power+2)
#         else:
#             if (foot_move[0] - current_number) == 2:
#                 dfs([current_number, foot_move[1]], idx+1, power+4)
#             else:
#                 dfs([current_number, foot_move[1]], idx+1, power+3)

#         if not foot_move[1]:            #오른발이 아직 가운데 있으면
#             dfs([foot_move[0], current_number], idx+1, power+2)
#         else:
#             if (foot_move[1] - current_number) == 2:
#                 dfs([foot_move[0], current_number], idx+1, power+4)
#             else:
#                 dfs([foot_move[0], current_number], idx+1, power+3)

# sequence = list(map(int, input().split()))

# sol = float('inf')
# foot_move = [0, 0]


# dfs(foot_move, 0, 0)

# print(sol)

def power(current_foot, current_number):
    if current_foot == current_number:              #현재 발의 위치랑 움직여야 하는 위치가 같은 경우
        return 1
    elif not current_foot:                          #발을 아직 떼지 않은 경우
        return 2
    elif abs(current_foot - current_number) == 2:   #반대편으로 가는 경우, 1, 2, 3, 4 순으로 가고 싶으면 abs(현 - 다음) == 1 or 현 * 다음 == 4  로 두면 됨
        return 4
    else:
        return 3

sequence = list(map(int, input().split()))
length = len(sequence)
dp = [[[float('inf') for _ in range(5)] for _ in range(5)] for _ in range(length+1)]

# 시행턴, 왼발, 오른발
dp[0][0][0] = 0 

for i in range(1, length):
    # 이동할 번호 
    move = sequence[i-1]

    # 25가지의 경우를 모두 고려 0, 1, 2, 3, 4 (0은 첫발만 나오지만, 첫발을 안 떼도 되기 때문에 지속적으로 고려해주자)
    # 왼발(5) * 오른발(5)
    for left in range(5):
        for right in range(5):
            # 왼발을 이동한 경우
            dp[i][move][right] = min(dp[i][move][right], dp[i-1][left][right] + power(left, move))
            # 오른발을 이동한 경우
            dp[i][left][move] = min(dp[i][left][move], dp[i-1][left][right] + power(right, move))

sol = float('inf')
for i in range(5):
    sol = min(sol, min(dp[-2][i]))

print(sol)
