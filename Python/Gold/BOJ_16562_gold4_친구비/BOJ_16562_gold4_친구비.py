# BOJ_16562_gold4_친구비

import sys
from collections import deque, defaultdict

input = sys.stdin.readline

def bfs():
    que = deque()
    visited = set()
    total_cost = 0
    friends = set(list(range(1,n+1)))

    # 모든 친구를 체크한다.
    while friends:
        cost = float('inf')
        node = friends.pop()       
        que.append(node)
        visited.add(node)
        # 해당 친구의 친구들을 체크
        while que:
            s = que.popleft()
            chk_cost = friends_cost[s]
            if cost > chk_cost:     # 친구의 친구들 중에 최소 비용 체크
                cost = chk_cost
            for i in graph[s]:
                if i not in visited:
                    que.append(i)
                    visited.add(i)
                    friends.discard(i)
        total_cost += cost          # 친구비를 갱신
        if total_cost > k:          # 총 비용이 k원보다 크면 'Oh np' 출력
            return 'Oh no'
    return total_cost         


n, m, k = map(int, input().split())
friends_cost = [0] + list(map(int, input().split()))


graph = defaultdict(list)

# 그래프 연결
for i in range(m):
    v, w = map(int, input().split())
    if v != w:
        graph[v].append(w)
        graph[w].append(v)

print(bfs())