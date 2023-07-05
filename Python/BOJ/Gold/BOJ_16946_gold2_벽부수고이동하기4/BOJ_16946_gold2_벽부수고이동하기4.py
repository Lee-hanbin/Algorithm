# BOJ_16946_gold2_벽부수고이동하기4

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

map1 = list(list(input().rstrip()) for _ in range(n))

#1. 시간초과

# idx_set = set()

# for i, e1 in enumerate(map1):
#     for j, e2 in enumerate(e1):
#         if e2 == '1':
#             idx_set.add((i, j))


# dr = [-1, 1, 0, 0]
# dc = [ 0, 0,-1, 1]

# answer = [['0'] * m for _ in range(n)]
# while idx_set:
#     sr, sc = idx_set.pop()
#     que = deque()
#     visited = set()
#     que.append((sr, sc))
#     visited.add((sr, sc))
#     cnt = 1
    
#     while que:
#         r, c = que.popleft()

#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited and map1[nr][nc] == '0':
#                 cnt += 1
#                 visited.add((nr, nc))
#                 que.append((nr, nc))
    
#     answer[sr][sc] = str(cnt%10)


# for i in answer:
#     print(''.join(i))

#2. 맵 2개 사용
idx_lst = []
idx_lst2 = []
for i, e1 in enumerate(map1):
    for j, e2 in enumerate(e1):
        if e2 == '0':
            idx_lst.append((i, j))
        else:
            idx_lst2.append((i, j))

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

answer = [[0] * m for _ in range(n)]

for sr, sc in idx_lst:
    que = deque()
    que.append((sr, sc))
    visited = set()
    visited.add((sr, sc))
    cnt = 1
    
    while que:
        r, c = que.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited and map1[nr][nc] == '0':
                cnt += 1
                visited.add((nr, nc))
                que.append((nr, nc))
    
    for rr, cc in list(visited):
        answer[rr][cc] = cnt

for sr, sc in idx_lst2:
    tmp = 1
    for i in range(4):
        nr = sr + dr[i]
        nc = sc + dc[i]
        
        if 0 <= nr < n and 0 <= nc < m:
            tmp += (answer[nr][nc]%10)
            
    map1[sr][sc] = tmp%10

for i in map1:
    print(''.join(map(str, i)))