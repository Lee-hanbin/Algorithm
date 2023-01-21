# BOJ_9663_gold4-NQUEEN

import sys

# 입력부
n = int(sys.stdin.readline())

# col : 열 방향 리스트
col = [False] * n

# diag1 : 대각선 방향 (우상 ~ 좌하) 방향 리스트
diag1 = [False] * (2 * n - 1)

# diag2 : 대각선 방향 (좌상 ~ 우하) 방향 리스트
diag2 = [False] * (2 * n - 1)

ans = 0

def go(i):
    global ans
    # base case : 모든 행이 조건을 만족했을 경우
    if i == n:
        ans += 1
        return
        
    # recursive case : 현재 i행에 대해 j열에서 퀸을 놓을 수 있는지 체크
    for j in range(n):
        # 만일 세 방향(열, 대각선1, 대각선2) 모두 다른 퀸들의 영향 밖이라면 재귀 호출
        if not col[j] and not diag1[i + j] and not diag2[i - j + n - 1]:
            # 현재 (i,j)에 의해 각 방향별로 영향을 받는 칸들을 True로 바꿈
            col[j] = True
            diag1[i + j] = True
            diag2[i - j + n - 1] = True
            
            # 재귀 호출
            go(i + 1)
            
            # backtrack
            col[j] = False
            diag1[i + j] = False
            diag2[i - j + n - 1] = False

# 함수 호출 및 정답 출력
go(0)
print(ans)
# def transpose(lst):
#     lst2 = []
#     for i in zip(*lst):
#         lst2.append(list(i))
#     return lst2

# def bfs(idx):
#     s_r, e_r = idx
    
    

# map1 = [[0] * n for _ in range(n)]



# for i in range(n):
#     map1[i] = [1] * n
#     map1 = transpose(map1)
#     for j in range(n):
#         map1[j] = [1] * n
#         for k in range(n):
#             if 0<= i + k < n:
#                 if 0<= j + k < n: 
#                     map1[i+k][j+k] = 1
#                 elif 0<= j - k < n:
#                     map1[i+k][j-k] = 1
#             elif 0<= i - k < n:
#                 if 0<= j + k < n: 
#                     map1[i-k][j+k] = 1
#                 elif 0<= j - k < n:
#                     map1[i-k][j-k] = 1
#                 map1[i+k][j-k] = 1
#         bfs((i, j))
        
