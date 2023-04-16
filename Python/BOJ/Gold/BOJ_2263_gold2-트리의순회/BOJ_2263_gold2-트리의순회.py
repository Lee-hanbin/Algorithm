import sys

input = sys.stdin.readline


#1. stack 2개 사용한 풀이 

N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

position = [0 for _ in range(N+1)]

# sol = []

for i in range(N):
    position[in_order[i]] = i

left_stack = []
right_stack = []

root_node = post_order[-1]
print(root_node, end=" ")
# sol.append(root_node)
root_node_idx = in_order.index(root_node)

# in_order index , post_order_index
if root_node_idx != 0:
    left_stack.append((0, root_node_idx-1, 0, root_node_idx-1))
if root_node_idx != N-1:
    right_stack.append((root_node_idx+1 , N-1, root_node_idx, N-2))


while left_stack or right_stack:
    if left_stack:
        in_first_idx, in_last_idx, post_first_idx, post_last_idx = left_stack.pop()
    else:
        in_first_idx, in_last_idx, post_first_idx, post_last_idx = right_stack.pop()

    if in_first_idx == in_last_idx and post_first_idx != post_last_idx:
        root_node = in_order[in_first_idx]
        root_node_idx = in_first_idx
        # sol.append(root_node)
        print(root_node, end=" ")
        continue

    #1. root 노드 출력
    root_node = post_order[post_last_idx]
    # sol.append(root_node)
    print(root_node, end=" ")

    #2. root 노드의 idx 찾기
    # root_node_idx = in_order.index(root_node)
    root_node_idx = position[root_node]

    l = root_node_idx - in_first_idx

    #3. stack에 왼쪽 서브트리 오른쪽 서브트리 idx 담기
    if root_node_idx != in_first_idx:
        left_stack.append((in_first_idx, root_node_idx - 1, post_first_idx, post_first_idx + l - 1 ))
    
    if root_node_idx != in_last_idx:
        right_stack.append((root_node_idx + 1, in_last_idx, post_first_idx + l , post_last_idx - 1))

# print(*sol)


# 2.재귀를 이용한 풀이

# import sys

# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline


# def find_tree(l_in, r_in, l_post, r_post):
#     if l_in > r_in or l_post > r_post:
#         return

#     root = post_order[r_post]
#     print(root, end=' ')
#     idx = position[root]
#     count = idx - l_in

#     # 왼쪽 서브트리 
#     find_tree(l_in, idx - 1, l_post, (l_post + count) - 1)
#     # 오른쪽 서브트리
#     find_tree(idx + 1, r_in, l_post + count, r_post - 1)
    
# N = int(input())
# in_order = list(map(int, input().split()))
# post_order = list(map(int, input().split()))
# position = [0 for _ in range(N+1)]

# for i in range(N):
#     position[in_order[i]] = i

# find_tree(0, N-1, 0, N-1)