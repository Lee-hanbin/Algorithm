# BOJ_7662_gold4-이중우선순위큐

import sys
from queue import PriorityQueue
from heapq import heappop, heappush
input = sys.stdin.readline
# sys.stdin = open('input.txt')

t = int(input())

for _ in range(t):
    I_cnt = 0
    D_cnt = 0
    big_cnt = 0
    small_cnt = 0

    que_big = []
    que_small = []
    # que_big = PriorityQueue()
    # que_small = PriorityQueue()
    n = int(input())

    visited = [0] * n
    
    for _ in range(n):
        command, num = input().split()
        num = int(num)
        if command == 'I':
            heappush(que_big, (-1 * num, I_cnt))
            heappush(que_small, (num, I_cnt))
            # que_big.put((-1 * num, I_cnt))
            # que_small.put((num, I_cnt))
            visited[I_cnt] = 1
            I_cnt += 1
        else:
            if I_cnt != D_cnt:      # 넣은 것과 뺀 것의 개수가 다르면
                D_cnt += 1          # 숫자를 pop 했으면 counting
                if num == 1:        # 큐에서 가장 높은 숫자 뽑기
                    for i in range(I_cnt - big_cnt):
                        if que_big:
                            tmp_big, tmp_big_idx = heappop(que_big)
                            # tmp_big, tmp_big_idx = que_big.get()
                            big_cnt += 1
                            if visited[tmp_big_idx]:        # 해당 숫자가 아직 안 뽑혔으면 그만 뽑아
                                visited[tmp_big_idx] = 0
                                break
                        else:
                            break
                else:               # 큐에서 가장 낮은 숫자 뽑기
                    for i in range(I_cnt - small_cnt):
                        if que_small:
                            tmp_small, tmp_small_idx = heappop(que_small)
                            # tmp_small, tmp_small_idx = que_small.get()
                            small_cnt += 1
                            if visited[tmp_small_idx]:
                                visited[tmp_small_idx] = 0
                                break
                        else:
                            break
            else:                   # 넣은 것과 뺀 것의 개수가 같으면 넘기기
                continue
    if I_cnt == D_cnt or not que_big or not que_small:
        print('EMPTY')
    else:

        max_num, max_num_idx = heappop(que_big)
        # max_num, max_num_idx = que_big.get()
        max_num *= -1
        while que_big and not visited[max_num_idx]:
            max_num, max_num_idx = heappop(que_big)
            # max_num, max_num_idx = que_big.get()
            max_num *= -1

        min_num, min_num_idx = heappop(que_small)
        # min_num, min_num_idx = que_small.get()
        while que_small and not visited[min_num_idx]:
            min_num, min_num_idx = heappop(que_small)
            # min_num, min_num_idx = que_small.get()

        print(max_num, min_num)

