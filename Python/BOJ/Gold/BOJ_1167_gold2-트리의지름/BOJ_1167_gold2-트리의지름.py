# BOJ_1167_gold2-트리의지름

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

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
target = set()
tree = defaultdict(list)
sol = 0

for _ in range(n):
    chk = list(map(int, input().split()))
    cur_node = chk[0]
    for i in range(1, len(chk)-1,2):
        next_node = chk[i]
        next_weight = chk[i+1]
        tree[cur_node].append((next_weight, next_node))

# 타겟을 지정
for i in tree.keys():
    if len(tree[i]) == 1:
        target.add(i)

# 루트인 1부터 시작하여 리프노드까지의 가치의 합이 가장 큰 리프노드 선택
node, dist = bfs(1)

# 해당 리프노드에서 출발하여 다른 리프노드까지 갔을 때, 가장 큰 가치를 출력
print(bfs(node)[1])