# BOJ_27172_gold5-수나누는게임

import sys

input = sys.stdin.readline

n = int(input())
player = list(map(int, input().split()))
player_check = [False] * 1000001
0
for i in player:
    player_check[i] = True

player_score = [0] * 1000001

for i in sorted(player):
    if i > 500000:
        break
    for j in range(i*2, 1000001, i):
        if player_check[j]:
            player_score[i] += 1
            player_score[j] -= 1

for i in player:
    print(player_score[i], end=" ")
# for i, e in enumerate(player):
#     for j in range(i+1, n):
#         if not e % player[j]:
#             player_score[i] -= 1
#             player_score[j] += 1
#         elif not player[j] % e:
#             player_score[j] -= 1
#             player_score[i] += 1

# print(*player_score)
