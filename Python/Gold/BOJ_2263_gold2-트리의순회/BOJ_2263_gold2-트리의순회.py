
def find_tree(l_in, r_in, l_post, r_post):
    if l_in > r_in or l_post > r_post:
        return

    root = post_order[r_post]
    print(root, end=' ')
    idx = position[root]
    count = idx - l_in

    # 왼쪽 서브트리 
    find_tree(l_in, idx - 1, l_post, (l_post + count) - 1)
    # 오른쪽 서브트리
    find_tree(idx + 1, r_in, l_post + count, r_post - 1)
    
N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
position = [0 for _ in range(N+1)]

for i in range(N):
    position[in_order[i]] = i

find_tree(0, N-1, 0, N-1)