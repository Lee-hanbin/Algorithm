# BOJ_2239_gold4-스도쿠

import sys

input = sys.stdin.readline


def search(idx):
    if idx == length:
        for i in map1:
            sol = ''
            for e in i:
                sol += str(e)
            print(sol)
        exit()

    r, c = idx_lst[idx]
    chk_set = set(range(1,10))
    # row 체크
    for v in map1[r]:
        if v > 0:
            chk_set.discard(v)
    # col 체크
    for v in map2[c]:
        if v > 0:
            chk_set.discard(v)    
    # 3 x 3 체크
    row = r // 3 * 3
    col = c // 3 * 3
    for rr in range(row, row+3):
        for cc in range(col, col+3):
            v = map1[rr][cc]
            if v > 0:
                chk_set.discard(v)

    # 가능한 모든 숫자 체크
    for n in chk_set:
        map1[r][c] = n
        map2[c][r] = n
        search(idx+1)
        map1[r][c] = 0
        map2[c][r] = 0



map1 = []
idx_lst = []

# 비어있는 칸 체크
for i in range(9):
    map1.append(list(map(int, input().rstrip())))
    for j, e in enumerate(map1[i]):
        if e == 0:
            idx_lst.append((i, j))
cnt = 0
map2 = []
for i in zip(*map1):
    map2.append(list(i))

length = len(idx_lst)

search(0)
# while idx_set:
#     idx_lst = list(idx_set)
#     for r, c in idx_lst:
#         chk_set = set(range(1, 10))
#         search(r, c)
#         if len(chk_set) == 1:
#             value = chk_set.pop()
#             map1[r][c] = value
#             map2[c][r] = value
#             idx_set.discard((r, c))





# def search(r, c):
#     for v in map1[r]:
#         if v > 0:
#             chk_set.discard(v)

#     for v in map2[c]:
#         if v > 0:
#             chk_set.discard(v)
    
#     row = r // 3 * 3
#     col = c // 3 * 3


#     for rr in range(3):
#         for cc in range(3):
#             v = map1[row + rr][col + cc]
#             if v > 0:
#                 chk_set.discard(v)


# map1 = []
# idx_set = set()
# for i in range(9):
#     map1.append(list(map(int, input().rstrip())))
#     for j, e in enumerate(map1[i]):
#         if e == 0:
#             idx_set.add((i, j))

# map2 = []
# for i in zip(*map1):
#     map2.append(list(i))

# while idx_set:
#     idx_lst = list(idx_set)
#     for r, c in idx_lst:
#         chk_set = set(range(1, 10))
#         search(r, c)
#         if len(chk_set) == 1:
#             value = chk_set.pop()
#             map1[r][c] = value
#             map2[c][r] = value
#             idx_set.discard((r, c))


# for i in map1:
#     sol = ''
#     for e in i:
#         sol += str(e)
#     print(sol)


# def dfs(target):
#     if target >= len(blank):
#         return 0
#     nx,ny = blank[target][0],blank[target][1]
#     if nx < 0 or nx >= 9 or ny < 0 or ny >= 9:
#         return 0
#     tmp = make_numbers(nx,ny)
#     for k in tmp:
#         board[ny][nx] = k
#         if dfs(target+1) == 0:
#             return 0
#         board[ny][nx] = 0
#     return 1

# def make_numbers(x,y):
#     res = []
#     for idx in range(1,10):
#         if is_right(x,y,idx):
#             res.append(idx)
#     return res

# def is_right(x,y,t):
#     for check in range(9):
#         if t == board[y][check]:
#             return False
#     for check in range(9):
#         if t == board[check][x]:
#             return False
#     xs = x // 3 * 3
#     ys = y // 3 * 3
#     for yn in range(ys, ys+3):
#         for xn in range(xs, xs+3):
#             if board[yn][xn] == t:
#                 return False
#     return True

# board = []
# blank = []

# for y in range(9):
#     board.append(list(map(int, list(input())[:9] )))
#     for x in range(9):
#         if board[y][x] == 0:
#             blank.append([x,y])

# dfs(0)

# for i in board:
#     sol = ''
#     for e in i:
#         sol += str(e)
#     print(sol)