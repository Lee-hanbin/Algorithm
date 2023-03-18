# BOJ_17136_gold2-색종이붙이기

import sys
input = sys.stdin.readline

def dfs(r, cnt):
    global sol

    # 모든 칸이 다 채워지면 갱신
    if not cnt:
        sol = min(sol, 25 - sum(paper))
        return

    # 색종이 채워 넣기
    for rr in range(r, 10):
        for c in range(10):
            if papers[rr][c]:

                # 크기에 맞는 색종이들을 넣기
                for n in range(1, 6):
                    chk = 0
                    if paper[n] > 0 and  rr + n < 11 and c + n < 11:

                        # 해당 영역의 크기를 확인
                        for i in range(rr, rr+n):
                            chk += sum(papers[i][c:c+n])

                        # 해당 영역에 색종이가 들어가면 색종이의 개수와 종이를 갱신해서 계속 진행
                        if chk == paper_size[n]:
                            paper[n] -= 1
                            for i in range(rr, rr+n):
                                papers[i][c:c+n] = [0] * n
                            dfs(rr, cnt - paper_size[n])
                            paper[n] += 1
                            for i in range(rr, rr+n):
                                papers[i][c:c+n] = [1] * n
                        
                        # 작은 색종이에서 막혔다면 굳이 큰 색종이 체크 x
                        else:
                            return 
                return
                


papers = list(list(map(int, input().split())) for _ in range(10))
paper = [0, 5, 5, 5, 5, 5]
paper_size = [0, 1, 4, 9, 16, 25]
sol = 26
tmp = 0

# 1이 있는 모든 영역 counting
for i in papers:
    for j in i:
        if j:
            tmp += 1

dfs(0, tmp)

if sol == 26:           # 불가능하면 -1
    print(-1)
else:                   # 가능하면 출력
    print(sol)