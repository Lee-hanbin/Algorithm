# BOJ_1389_silver1-케빈 베이컨의 6단계 법칙

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def bfs(s, target):
    que = deque()
    visited = set()
    que.append((s, 1))
    visited.add(s)
    while que:
        node, cnt = que.popleft()
        if node == target:
            return cnt
        for i in graph[node]:
            if i not in visited:
                que.append((i, cnt + 1))
                visited.add(i)
    

N, M = map(int, input().split())

graph = defaultdict(list)
cnt_lst = [0] * (N+1)


for i in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, N+1):         # 1 ~ N 을 모두 순회
    for j in range(1, N+1):     # i가 아닌 값에 대해서 1 ~ N 을 모두 순회
        cnt = float('inf')      # 최소 cnt 
        if i == j:
            continue
        for k in graph[i]:      # i와 연결된 노드들 순회
            if k == j:          # target과 연결된 노드가 같으면 1 출력
                cnt = 1
                break
            else:
                chk = bfs(k, j) # bfs를 통해 counting
                if cnt > chk:   # cnt 최소값 갱신
                    cnt = chk
                    
        cnt_lst[i] += cnt

sol_cnt = min(cnt_lst[1:])
sol_idx = cnt_lst.index(sol_cnt)
print(sol_idx)