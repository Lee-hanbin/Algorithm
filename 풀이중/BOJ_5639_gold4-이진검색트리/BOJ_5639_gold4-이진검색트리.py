# # BOJ_5639_gold4-이진검색트리
#
# import sys
# from collections import defaultdict
# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline
#
#
# def postorder(n):
#     if n:
#         postorder(tree[n][1])
#         postorder(tree[n][2])
#         print(n)
#
#
# tree = defaultdict()
# lst = []
# # for node in sys.stdin:
# #     lst.append(node)
# for i in range(17):
#     lst.append(int(input().strip()))
# root = lst[0]
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
#
#
