# BOJ_16234_gold5-인구이동

import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

def bfs(r, c):
    switch = 0              # 연합여부
    que = deque()
    que.append((r,c))
    people = [(r, c)]       # 연합하는 나라의 인덱스
    union = country[r][c]   # 연합하는 나라의 인구수
    visited[r][c] = 1         # 방문 표시
    # bfs 진행
    while que:
        r, c = que.popleft()
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if 0 <= nr < n and 0 <= nc < n and L<= abs(country[r][c] - country[nr][nc]) <=R and not visited[nr][nc]:
                switch = 1
                que.append((nr, nc))
                people.append((nr, nc))
                union += country[nr][nc]
                visited[nr][nc] = 1
    # 연합이 생성되면 인구이동 시작
    if switch:
        union_people = union // len(people)
        for rr, cc in people:
            country[rr][cc] = union_people
    return switch 

n, L, R = map(int, input().split())

country = [list(map(int, input().split())) for _ in range(n)]

sol = 0
while 1:
    chk = 0
    visited = [[0]*n for _ in range(n)]
    # 전체 순회
    for r in range(n):
        for c in range(n):
            if not visited[r][c] and bfs(r, c):         # 방문하지 않고 연합이 생성된 경우
                chk = 1
    if chk:
        sol += 1
    else: 
        break

print(sol)