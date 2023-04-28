# BOJ_4803_gold4-트리

import sys

inpurt = sys.stdin.readline

def find_parents(parent, node):
    if parent[node] != node:
        parent[node] = find_parents(parent, parent[node])
    return parent[node]

def union_parent(parent, a, b):
    a = find_parents(parent, a)
    b = find_parents(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

case = 0

while 1:
    n, m = map(int, input().split())
    parent = [0] * (n + 1)
    sol_set = set()
    cycle_set = set()
    
    if not n:
        break
    else:
        case += 1
            
        for i in range(1, n+1):
            parent[i] = i
        
        for _ in range(m):
            s, e = map(int, input().split())
            
            if s in cycle_set or e in cycle_set or find_parents(parent, s) == find_parents(parent, e):
                cycle_set.add(find_parents(parent, s))
            else:
                union_parent(parent, s, e)
        
    sol_set = set(parent)
    # print(cycle_set)
    # print(sol_set)
    
    sol_set = sol_set - cycle_set
    sol = len(sol_set) - 1
    
    if not sol:
        print(f'Case {case}: No trees.')
    elif sol == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {sol} trees.')