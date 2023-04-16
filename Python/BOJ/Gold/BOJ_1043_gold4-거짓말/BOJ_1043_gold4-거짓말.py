# BOJ_1043_gold4-거짓말

import sys

input = sys.stdin.readline

n,m = map(int, input().split())

# cnt = 0

set_real = set(list(map(int, input().split()))[1:])
lst_party = [list(map(int, input().split())) for _ in range(m)]
visited = [1] * m
switch = 1

# 사실이 파티장에 퍼지지 않을때까지 반복
while switch:
    for i, e in enumerate(lst_party):
        set_party = set(e[1:])
        intersection = set_party & set_real
        
        # 진실을 알고 있는 사람이 있는 파티장의 경우, 사실 리스트를 갱신 
        if intersection and visited[i]:
            set_real = set_real | set_party
            visited[i] = 0
            break
    else:
        switch = 0

print(sum(visited))

# for i in lst_party:
#     set_party = set(i[1:])
#     intersection = set_party & set_real
#     if not intersection:
#         cnt += 1
        
# print(cnt)