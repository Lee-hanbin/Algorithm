# BOJ_9466_gold3-텀프로젝트

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# dfs 없이 반복문 구현...
t = int(input())

for _ in range(t):
    n = int(input())

    sol = 0
    team = [0] + list(map(int, input().split()))

    visited = set()
    for i in range(1, n+1):
        if i not in visited:
            idx = i
            while idx not in visited:
                visited.add(idx)
                idx = team[idx]
            current = i
            while current != idx:
                sol += 1
                current = team[current]
    print(sol)


# set이 생각보다 비효율적임... 특히, 합집합이나 차집합은 O(n + m) 이라는 점이 크리티컬
def dfs(node):
    global final
    if node in visited:
    # if visited[node]:
        final = node
        return
    visited.add(node)
    # visited[node] = 1
    dfs(team[node])


t = int(input())

for _ in range(t):
    n = int(input())

    cycle_set = set()
    sol_set = set()
    team = [0] + list(map(int, input().split()))
    # for s, e in enumerate(team):
    #     if s == e:
    #         cycle_set.add(s)

    # for s, e in enumerate(team):
    #     if s != e and e in cycle_set:
    #         sol_set.add(s)

    for i in range(1, n+1):
        visited = set()
        # visited = [0] * (n + 1)
        final = 0
        if i not in sol_set and i not in cycle_set:
            visited.add(i)
            # visited[i] = 1
            dfs(team[i])
            if final == i:
                while visited:
                    cycle_set.add(visited.pop())
            else:
                sol_set.add(i)
    print(len(sol_set))

# # 단순 사이클 구하는 문제 x => union find 불가
# def find(node):
#     if parent[node] != node:
#         parent[node] = find(parent[node])
#     return parent[node]

# def union(s, e):
#     s = find(s)
#     e = find(e)

#     if s < e:
#         parent[e] = s
#     else:
#         parent[s] = e


# t = int(input())

# for _ in range(t):
#     n = int(input())
    
#     parent = [0] * (n+1)

#     for i in range(1, n+1):
#         parent[i] = i

#     mine_set = set()
#     cycle_set = set()
#     sol_set = set()
#     team = list(map(int, input().split()))

#     for i, e in enumerate(team):
#         s = i+1
#         if s == e:
#             mine_set.add(s)

#     for i, e in enumerate(team):
#         s = i + 1
#         if s != e and e in mine_set:
#             sol_set.add(s)

#     for i, e in enumerate(team):
#         s = i + 1
#         if s in sol_set:
#             continue


#         if find(s) == find(e):
#             cycle_set.add(parent[s])
#         else:
#             union(s, e)
#             # if s in cycle_set or e in cycle_set:
#             #     cycle_set.add(parent[s])


#     for i in range(1, n+1):
#         find(i)
#     cnt = 0
#     for i in range(1, n+1):
#         if parent[i] in cycle_set or i in mine_set:
#             continue
#         cnt += 1 

#     print(mine_set)
#     print(cycle_set)
#     print(sol_set)
#     print(parent)
#     print(cnt)