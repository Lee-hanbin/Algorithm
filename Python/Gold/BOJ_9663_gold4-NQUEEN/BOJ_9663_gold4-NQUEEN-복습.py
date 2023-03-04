# BOJ_9663_gold4-NQUEEN

import sys

input = sys.stdin.readline

def backtracking(r):
    global sol

    if r == n:  
        sol += 1
        return 
    
    for c in range(n):
        # left_idx = (r+c)
        # right_idx = (r-c+n-1)
        if not col_lst[c] and not diagonal_left[r+c] and not diagonal_right[r-c+n-1]: 
            col_lst[c] = 1
            diagonal_left[r+c] = 1
            diagonal_right[r-c+n-1] = 1

            backtracking(r+1)

            col_lst[c] = 0
            diagonal_left[r+c] = 0
            diagonal_right[r-c+n-1] = 0


n = int(input())

sol = 0

diagonal_left = [0] * (2 * n - 1)
diagonal_right = [0] * (2 * n - 1)
col_lst = [0] * n


backtracking(0)
print(sol)