# BOJ_1967_gold4-트리의지름

import sys
from collections import defaultdict, deque
from itertools import combinations
input = sys.stdin.readline


#######################################################################################################

#1. n : 리프노드 개수 => nC2 로 모든 리프노드의 지름 구하기

def search(idx):
    start, end = idx
    que = deque()
    visited = set()
    visited.add(start)
    que.append((start, 0))
    while que:
        start, w = que.popleft()
        if start == end:
            return w
        for i in tree[start]:
            if i[1] not in visited:
                visited.add(i[1])
                que.append((i[1], w + i[0]))
    return 0

n = int(input())
V = n-1

tree = defaultdict(list)
target = []
sol = 0

for i in range(V):
    s, e, w = map(int, input().split())
    tree[s].append((w, e))
    tree[e].append((w, s))

# 리프노드 탐색
for i in tree.keys():
    if len(tree[i]) == 1:
        target.append(i)
    tree[i].sort(key= lambda x: x[0])

# 리프노드의 시작점과 끝점 탐색
for i in combinations(target, 2):
    chk = search(i)
    if sol < chk:
        sol = chk
print(sol)

#######################################################################################################

#2. bfs 이용하여 리프노드 당 한번만 탐색

def bfs(idx):
    chk = 0
    que = deque()
    visited = set()
    visited.add(idx)
    que.append((idx, 0))
    while que:
        start, w = que.popleft()
        for i in tree[start]:
            if i[1] not in visited:
                if i[1] in target:
                    if chk < w + i[0]:
                        chk = w + i[0]
                    continue
                visited.add(i[1])
                que.append((i[1], w + i[0]))

    return chk


n = int(input())
V = n-1

tree = defaultdict(list)
target = set()
sol = 0

# 트리 생성
for i in range(V):
    s, e, w = map(int, input().split())
    tree[s].append((w, e))
    tree[e].append((w, s))

# 리프노드 찾기
for i in tree.keys():
    if len(tree[i]) == 1:
        target.add(i)

# 리프노드로 탐색
for i in list(target):
    chk = bfs(i)
    if sol < chk:
        sol = chk

print(sol)

#######################################################################################################

#3. 루트노드를 기준으로 리프노드를 선정하여 하나의 리프노드만 bfs


def bfs(idx):
    chk = [0, 0]
    que = deque()
    visited = set()
    visited.add(idx)
    que.append((idx, 0))
    while que:
        start, w = que.popleft()
        for i in tree[start]:
            if i[1] not in visited:
                if i[1] in target:
                    if chk[1] < w + i[0]:
                        chk = i[1], w + i[0]
                    continue
                visited.add(i[1])
                que.append((i[1], w + i[0]))

    return chk


n = int(input())
V = n-1

tree = defaultdict(list)
target = set()

# 트리 생성
for i in range(V):
    s, e, w = map(int, input().split())
    tree[s].append((w, e))
    tree[e].append((w, s))

# 타겟을 지정
for i in tree.keys():
    if len(tree[i]) == 1:
        target.add(i)

# 루트인 1부터 시작하여 리프노드까지의 가치의 합이 가장 큰 리프노드 선택
node, dist = bfs(1)

# 해당 리프노드에서 출발하여 다른 리프노드까지 갔을 때, 가장 큰 가치를 출력
print(bfs(node)[1])
