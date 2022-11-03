# BOJ_5639_gold4-이진검색트리

# import sys
from collections import defaultdict, deque


# def postorder(n):
#     if n:
#         postorder(tree[n][1])
#         postorder(tree[n][2])
#         print(n)
from bisect import bisect_left
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def bi_search(start, end, target):
    res = end
    while True:
        mid = (start + end)//2
        if lst[mid] < target:
            start = mid + 1
            res = mid
        else:
            end = mid - 1
        if start > end:
            break
    return res

def post(start, end):
    if start > end:
        return
    # 값이 하나면 출력
    if start == end:
        print(lst[start])
        return
    # 바이너리 서치로 서브트리의 루트 찾기
    root = bi_search(start + 1, end, lst[start])

    # 후위 순회
    post(start+1, root)
    post(root+1, end)
    print(lst[start])

lst = []
for node in sys.stdin:
    if node == '\n':
        break
    lst.append(int(node))
if lst:
    post(0, len(lst)-1)
# tree = defaultdict()
# que = deque()
# left_tree = []
# right_tree = []
# root = 0
# i = 0

#     i += 1
#     if i == 1:
#         root =  node
#         continue
#     if node < root:
#         left_tree.append(node)
#     else:
#         right_tree.append(node)
# for i in range(9):
#     que.append(int(input()))
# root = que.popleft()
# stack = [root]
# tree[root] = [-1, 0, 0]
# while que:
#     node = que.popleft()
#     tree[node] = [0,0,0]
#     if stack[-1] > node:
#         stack.append(node)
#     else:
#         while stack:
#             chk_node = stack.pop()
#             if chk_node < node:
#                 tree[chk_node][0] = stack[-1]
#                 tree[stack[-1]][1] = chk_node
#             else:

#
# left_tree
#
# print(root)
# print(left_tree)
# print(right_tree)









# tree[root] = [-1, 0, 0]
# flag = 0
# for i in range(1,len(lst)):
#     node = lst[i]
#     before_node = lst[i-1]
#     tree[node] = [0, 0, 0]
#     if node > root and flag == 0:
#         flag = 1
#         tree[root][2] = node
#         tree[node][0] = root
#         continue
#     if node < before_node:              # 작으면 좌측노드
#         tree[before_node][1] = node
#         tree[node][0] = before_node     # 부모노드체크
#     else:
#         if tree[before_node][1] == 0 and tree[before_node][0] >node > before_node:
#             tree[before_node][2] = node
#             tree[node][0] = before_node
#         else:
#             while 1:
#                 before_node = tree[before_node][0]
#                 if before_node < node < tree[before_node][0] or before_node > tree[before_node][0]:
#                     tree[before_node][2] = node
#                     tree[node][0] = before_node
#                     break
# print(tree)
# postorder(root)


