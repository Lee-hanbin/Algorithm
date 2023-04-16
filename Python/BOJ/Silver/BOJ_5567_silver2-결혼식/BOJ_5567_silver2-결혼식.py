# BOJ_5567_silver2-결혼식

import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = defaultdict(list)

# 그래프 연결
for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
visited = set()
visited.add(1)
cnt = 0

# 상근이의 친구 카운팅
for i in graph[1]:
    if i not in visited:
        visited.add(i)
        cnt += 1
    
    # 상근이의 친구의 친구 카운팅
    for j in graph[i]:
        if j not in visited:
            visited.add(j)
            cnt += 1

print(cnt)



# 1.단순하게 2. 팀 공감대 3.우선순위 분명 4.충분한 시드 머니 5. 플랜 ABCD