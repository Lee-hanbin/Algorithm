# BOJ_2536_gold1-버스갈아타기

import sys
from collections import deque


# bfs 
def bfs(start_r, start_c):
    que = deque()
    visited = set()

    # 해당 시작점이 해당 버스 노선안에 있을 경우, 모두 que에 넣는다.
    for nosun, idx in enumerate(station):
        if nosun == 0:
            continue
        s1, e1, s2, e2  = idx
        if s1 <= start_r <= s2 and e1 <= start_c <= e2:
            que.append((1, nosun))
            visited.add(nosun)
    while que:
        cnt, bus = que.popleft()
        s1, e1, s2, e2 = station[bus]
        
        # 해당 버스 노선안에 도착점이 존재할 경우 멈추고 cnt를 반환
        if s1 <= e_r <= s2 and e1 <= e_c <= e2:
            return cnt

        # 모든 버스 노선을 돌면서 아직 돌지 않은 버스노선 체크
        for chk_nosun in range(1, k+1):
            if chk_nosun not in visited:
                ss1, ee1, ss2, ee2 = station[chk_nosun]
                
                # 다음 버스 노선이 현재 버스 노선 밖으로 벗어나지 않는 경우 que에 넣고 환승
                if s1 <= ss2 and s2 >= ss1 and e1 <=ee2 and e2 >= ee1:
                    visited.add(chk_nosun)
                    que.append((cnt+1, chk_nosun))

input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())

station = [0] * (k+1)

# 모든 버스 노선의 정보를 작은 숫자 -> 큰 숫자로 입력받기
for _ in range(k):
    b, s1, e1, s2, e2 = map(int, input().split())
    if s1 == s2:
        station[b] = [s1, min(e1, e2), s2, max(e1, e2)]
    else:
        station[b] = [min(s1, s2), e1, max(s1, s2), e2]

s_r, s_c, e_r, e_c = map(int, input().split())

print(bfs(s_r, s_c))

# dr = [-1, 1, 0, 0]
# dc = [ 0, 0,-1, 1]

# def bfs(idx):
#     que = deque()
#     visited = set()
#     r, c, s, e = idx
#     sol = []
#     visited.add((r, c))
#     for i in station[r][c]:
#         que.append((i, r, c, 1, visited))
#     while que:
#         bus, r, c, cnt, visited_chk = que.popleft()
#         for i in range(4):
#             nr = dr[i] + r
#             nc = dc[i] + c
#             if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited_chk and station[nr][nc]:
#                 if (nr, nc) == (s, e):
#                     sol.append(cnt + 1)
#                 visited = visited_chk | {(nr,nc)}
#                 for nosun in station[nr][nc]:
#                     if nosun == bus:
#                         que.append((nosun, nr, nc, cnt, visited))
#                     else:
#                         que.append((nosun, nr, nc, cnt+1, visited))
#     return sol

# input = sys.stdin.readline

# n, m = map(int, input().split())
# k = int(input())

# # bus_nosun = defaultdict(list)
# station = [[[] for _ in range(m)] for _ in range(n)]
# for _ in range(k):
#     b, s1, e1, s2, e2 = map(int, input().split())
#     if s1 == s2:
#         for i in range(min(e1,e2)-1, max(e1,e2)):
#             station[s1-1][i].append(b)
#     else:
#         for i in range(min(s1, s2)-1, max(s1, s2)):
#             station[i][e1-1].append(b)

# s_r, s_c, e_r, e_c = map(int, input().split()) 


# print(min(bfs((s_r-1, s_c-1, e_r-1, e_c-1))))