# BOJ_16724_gold3-피리부는사나이

#2. set 대신 2차원 리스트로 visited를 설정하고 배열의 값으로 counting
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

map1 = list(list(input().rstrip()) for _ in range(n))


dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]
check_dict = {
    'U': 0,
    'D': 1,
    'L': 2,
    'R': 3
}

sol = 0
visited = [[0] * m for _ in range(n)]

cnt = 0
for r in range(n):
    for c in range(m):    
        if visited[r][c]:
            continue
        cnt += 1
        nr, nc = r, c
        while 1:
            if visited[nr][nc]:
                if visited[nr][nc] == cnt:
                    sol += 1
                break
            visited[nr][nc] = cnt
            nr = nr + dr[check_dict[map1[nr][nc]]]
            nc = nc + dc[check_dict[map1[nr][nc]]]

print(sol)


#1. set 두 개를 이요한 풀이.. 시간초과
n, m = map(int, input().split())

map1 = list(list(input().rstrip()) for _ in range(n))


dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

check_dict = {
    'U': 0,
    'D': 1,
    'L': 2,
    'R': 3
}

sol = 0
sol_set = set()

for r in range(n):
    for c in range(m):
        visited_set = set()
        visited_set.add((r, c))
        nr, nc = r, c
        while 1:
            nr = nr + dr[check_dict[map1[nr][nc]]]
            nc = nc + dc[check_dict[map1[nr][nc]]]

            if (nr, nc) in sol_set:
                break

            if (nr, nc) in visited_set:
                sol += 1
                break
            visited_set.add((nr, nc))

        sol_set = sol_set | visited_set
print(sol)