# BOJ_3665_gold1-최종순위

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    graph = defaultdict(list)
    before_rank = list(map(int, input().split()))
    visited = set()
    # node간 간선연결
    for i in range(n):
        for j in range(i+1,n):
            graph[before_rank[i]].append(before_rank[j])
    graph[before_rank[-1]]
    # 등수 변경에 의한 간선 뒤집기
    # print(graph)

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if b in graph[a]:
            graph[a].pop(graph[a].index(b))
            graph[b].append(a)
        else:
            graph[b].pop(graph[b].index(a))
            graph[a].append(b)


    # print(graph)
    
    # after_rank 찾기
    after_rank = [0] * n
    for k, v in graph.items():
        after_rank[n-len(v)-1] = k
    if 0 in after_rank:
        print('IMPOSSIBLE')
    else:
        print(*after_rank)        
 

##### 1. 구현 실패
# t = int(input())
# for _ in range(t):
#     n = int(input())

#     after_rank = [0] * (n+1)
#     before_rank = [0] +list(map(int, input().split()))

#     nonfix_team = set()
#     fix_team = set(range(1,n+1))

#     upcounting = [0] * (n+1)

#     check_list = []

#     # 조정이 있는 팀은 앞에 올 수 있는 팀의 수를 헤아린다
#     m = int(input())
#     for _ in range(m):
#         up, down = map(int, input().split())
#         nonfix_team.add(up)
#         nonfix_team.add(down)
#         if before_rank.index(up) < before_rank.index(down):     # 이전에 up이 down보다 컸으면
#             check_list.append((down, up))                       # 이후에는 down이 up보다 크다
#             upcounting[up] += (1 + upcounting[down])
#         else:
#             check_list.append((up, down))                       # 이후에는  up이 down보다 크다
#             upcounting[down] += (1 + upcounting[up])

#     fix_team = fix_team - nonfix_team
#     rank_set = set()
#     nonrank = set(range(1, n+1))
#     dict_chk = defaultdict(list)

#     # 조정 없는 팀을 fix & 조정 있는 팀은 앞에 올 수 있는 팀 수 담기
#     for team in range(1, n+1):
#         rank = before_rank.index(team)
#         if team in fix_team:
#             after_rank[rank] = team
#             rank_set.add(rank)
#         else:
#             dict_chk[upcounting[team]].append([rank, team])
#     nonrank = nonrank - rank_set
#     nonrank = sorted(list(nonrank))
#     max_rank = len(nonrank)

#     if not nonfix_team:             # 조정이 없으면 바로 출력
#         print(*before_rank[1:])
#     else:                           # 조정이 있으면
#         front = 0
#         try: 
#             while front < max_rank:                         # 앞에 올 수 있는 팀의 수 만큼 순회
#                 if len(dict_chk[front]) > 1:                # 앞에 올 수 있는 팀의 수가 같은 경우
#                     cnt = 0
#                     select_lst = []
#                     for i in dict_chk[front]:
#                         last_rank, team = i
#                         if last_rank == nonrank[front]:     # 해당 팀이 이전 등수와 같은 경우는 밀기 
#                             dict_chk[front+1].append(i)
#                             dict_chk[front].pop(cnt)
#                             front += 1
#                             break
#                         elif last_rank == nonrank[front+1]: # 만약 한 칸 밀렸을 때, 팀의 등수가 조정 전과 같으면 유지
#                             cnt +=1
#                             continue    
#                         else:                               # 다르다면 한 칸 뒤로 밀기
#                             select_lst.append((front, i, cnt))
#                             cnt += 1
#                     else:
#                         for k in select_lst:
#                             front2, i2, cnt2 = k
#                             dict_chk[front2+1].append(i2)
#                             dict_chk[front2].pop(cnt2)
#                             front += 1
                    
#                 else:                                       # 해당하는 등수의 팀이 하나이면 패스
#                     front += 1   

#             # 팀의 수를 다 헤아렸으면 등수 지정
#             for i, rank in enumerate(nonrank):
#                 team = dict_chk[i][0][1]
#                 after_rank[rank] = team
#                 if after_rank[rank] == before_rank[rank]:   # 만약, 조정했는데도 등수가 같으면 실패
#                     print('IMPOSSIBLE') 
#                     break
#                 fix_team.add(team)
#                 nonfix_team.discard(team)
#             else:
#                 # print(after_rank)
#                 for up, down in check_list:
#                     if after_rank.index(up) > after_rank.index(down):
#                         print('IMPOSSIBLE') 
#                         break
#                 else:
#                     print(*after_rank[1:])
#         except:
#             print('IMPOSSIBLE') 


# from collections import deque
# import sys

# t = int(sys.stdin.readline())

# for i in range(t):
#     n = int(sys.stdin.readline())

#     graph = [[] for _ in range(n + 1)]
#     inDegree = [0 for _ in range(n + 1)]
#     queue = deque()
#     answer = []
#     flag = 0

#     team = list(map(int, sys.stdin.readline().rstrip().split()))

#     for j in range(n - 1):
#         for k in range(j + 1, n):
#             graph[team[j]].append(team[k])
#             inDegree[team[k]] += 1

#     m = int(sys.stdin.readline())
#     for j in range(m):
#         first, second = map(int, sys.stdin.readline().rstrip().split())
#         flag = True

#         for k in graph[first]:
#             if k == second:
#                 graph[first].remove(second)
#                 inDegree[second] -= 1
#                 graph[second].append(first)
#                 inDegree[first] += 1
#                 flag = False

#         if flag:
#             graph[second].remove(first)
#             inDegree[first] -= 1
#             graph[first].append(second)
#             inDegree[second] += 1

#     for j in range(1, n + 1):
#         if inDegree[j] == 0:
#             queue.append(j)

#     if not queue:
#         print("IMPOSSIBLE")
#         continue

#     result = True
#     while queue:
#         if len(queue) > 1:
#             result = False
#             break

#         tmp = queue.popleft()
#         answer.append(tmp)
#         for j in graph[tmp]:
#             inDegree[j] -= 1
#             if inDegree[j] == 0:
#                 queue.append(j)
#             elif inDegree[j] < 0:
#                 result = False
#                 break

#     if not result or len(answer) < n:
#         print("IMPOSSIBLE")
#     else:
#         print(*answer)                        

