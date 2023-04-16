# BOJ_4485_gold4-녹색옷입은애가젤다지

import sys
import heapq

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

def dijkstra(r, c):
    dist = [[float('inf')] * n for _ in range(n)]
    dist[r][c] = map1[r][c]
    hq = []
    heapq.heappush(hq, [map1[0][0], 0, 0])

    while hq:
        now_w, now_r, now_c = heapq.heappop(hq)

        if dist[now_r][now_c] < now_w:
            continue 
        for i in range(4):
            nr = dr[i] + now_r
            nc = dc[i] + now_c
            if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] > dist[now_r][now_c] + map1[nr][nc]:
                dist[nr][nc] = dist[now_r][now_c] + map1[nr][nc]
                heapq.heappush(hq, [dist[nr][nc], nr, nc])

    return dist[n-1][n-1]

t = 0
while 1:
    n = int(input())
    if not n:
        break
    t += 1
    map1 = [list(map(int, input().split())) for _ in range(n)]
    print(f'Problem {t}: {dijkstra(0, 0)}')
