# BOJ_4803_gold4-트리

import sys

input = sys.stdin.readline

def union_parent(a, b):
    a = find_parents(a)
    b = find_parents(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parents(node):
    if parent[node] != node:
        parent[node] = find_parents(parent[node])
    return parent[node]


case = 0

while 1:
    n, m = map(int, input().split())
    
    if n==0 and m==0:
        break
    else:
        case += 1
        sol_set = set()
        cycle_set = set()
        parent = [0] * (n + 1)            
        for i in range(1, n+1):
            parent[i] = i
        
        for _ in range(m):
            s, e = map(int, input().split())
            
            if find_parents(s) == find_parents(e):
                cycle_set.add(parent[s])
            else:
                union_parent(s, e)
                if s in cycle_set or e in cycle_set:
                    cycle_set.add(parent[s])


    # find 함수를 쭉 돌려서 각 정점의 parent를 갱신한다.
    for i in range(n+1):
        find_parents(i)

    sol_set = set(parent)
    sol_set = sol_set - cycle_set
    sol = len(sol_set) - 1

    if not sol:
        print(f'Case {case}: No trees.')
    elif sol == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {sol} trees.')