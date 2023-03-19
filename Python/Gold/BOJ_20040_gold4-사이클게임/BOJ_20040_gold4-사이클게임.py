# BOJ_20040_gold4-사이클게임

import sys

# 특성 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾기 
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])  # 경로 압축
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 작은값이 부모루트가 되도록 지정
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

        
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i


for i in range(m):
    s, e = map(int, input().split())

    # 즉, 루트노드가 같으면 사이클
    if find_parent(parent,s) == find_parent(parent, e):
        print(i+1)
        break
    # 다르면 두 노드 중에 부모 노드가 될 노드를 지정해줌
    else:
        union_parent(parent,s,e)
else:
    print(0)