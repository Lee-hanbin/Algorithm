# SWEA_4615_재밌는오셀로게임

import sys

sys.stdin = open("sample_input.txt")

dr = [0, 0, 1,-1, 1, 1,-1,-1]
dc = [1,-1, 0, 0, 1,-1, 1,-1]


# 오셀로 한 수
def play(r, c, color):
    # 뒤집을 돌
    color_chk= 2 if color % 2 else 1
        
    map1[r][c] = color
    stone_cnt[color] += 1

    # 뒤집을 돌 탐색
    for i in range(8):
        nr = dr[i] + r
        nc = dc[i] + c
        idx_lst = [(nr, nc)]        #뒤집을 돌들의 list
        if 0 <= nr < n and 0 <= nc < n and map1[nr][nc] == color_chk:
            while 1:
                nr += dr[i]
                nc += dc[i]
                if 0 <= nr < n and 0 <= nc < n:
                    # 빈칸이 나오면 pass
                    if map1[nr][nc] == 0:
                        break
                    # 뒤집을 돌이 나오면 list에 넣기
                    elif map1[nr][nc] == color_chk:
                        idx_lst.append((nr,nc))
                    # 처음 뒀던 돌이 나오면 list에 담긴 돌 모두 뒤집기
                    else:
                        for rr, cc in idx_lst:
                            map1[rr][cc] = color
                            stone_cnt[color] += 1
                            stone_cnt[color_chk] -= 1
                        break
                else:
                    break


for t in range(1, int(input())+1):
    stone_cnt = [0, 2, 2]
    n, m = map(int, input().split())

    map1 = list([0] * n for _ in range(n))

    # 초기값 설정
    chk = n//2
    map1[chk-1][chk-1] = 2
    map1[chk-1][chk] = 1
    map1[chk][chk-1] = 1
    map1[chk][chk] = 2

    # 게임 진행
    for _ in range(m):
        r, c, color = map(int, input().split())
        play(r-1, c-1, color)

    print(f'#{t} {stone_cnt[1]} {stone_cnt[2]}')