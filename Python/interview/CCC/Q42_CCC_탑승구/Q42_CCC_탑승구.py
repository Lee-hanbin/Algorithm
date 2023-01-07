# Q42_CCC_탑승구

import sys
from collections import defaultdict

input = sys.stdin.readline

def union(a_set, b_set):
    global cnt
    if a_set - b_set:       # 차집합이 존재 => 뒤에 나오는 출입구에 다른 비행기가 도킹 가능
        cnt += 1


G = int(input())
P = int(input())

graph = defaultdict(list)

visited = set()
for i in range(1, P+1):
    door = int(input())
    for j in range(1, door+1):          # 각 탑승구에 도킹 가능한 비행기 체크
        graph[j].append(i)

cnt = 1                     # 첫 탑승구는 무조건 이용가능하니까 1부터 시작

for i in range(G):          # 인접한 두 탑승구의 차집합 구함
    union(set(graph[i]), set(graph[i+1]))

print(cnt)