# BOJ_13460_gold1-구슬탈출2

import sys
input = sys.stdin.readline


n, m = map(int, input().split())

map1 = list(list(input().rstrip()) for _ in range(n))

# for i in map1:
#     print(*i)
# print()

for i, e in enumerate(map1):
    for j, e2 in enumerate(e):
        if e2 == "R":
            startRed = (i, j)
            continue
        if e2 == "B":
            startBlue = (i, j)
            continue
        if e2 == "O":
            finish = (i, j)

dr = [-1, 1, 0, 0]
dc = [ 0, 0,-1, 1]

visited = set()
visited.add((startRed, startBlue))
sol = float('inf')

def back(red:tuple, blue:tuple, cnt:int):
    if cnt == 10:
        return
    
    for i in range(4):
        nrRed = dr[i] + red[0]
        ncRed = dc[i] + red[1]
        nrBlue = dr[i] + blue[0]
        ncBlue = dc[i] + blue[1]
        if ((nrRed, ncRed), (nrBlue, ncBlue)) not in visited:
            flag = 0
            switch = 0
            redStr, blueStr = map1[nrRed][ncRed], map1[nrBlue][ncBlue]
            nextRed, nextBlue = (nrRed, ncRed), (nrBlue, ncBlue)

            # 파란공 체크
            while blueStr != "#" and blueStr != "R":
                if blueStr == "O":
                    flag = 1
                    break
                nextBlue = (nextBlue[0] + dr[i], nextBlue[1] + dc[i])
                blueStr = map1[nextBlue[0]][nextBlue[1]]
            nextBlue = (nextBlue[0] - dr[i], nextBlue[1] - dc[i])
            if flag == 1:
                continue
            if blueStr == "R":
                flag = 2

            # 빨간공 체크
            while redStr != "#" and redStr != "B":
                if redStr == "O":
                    switch = 1
                    break
                nextRed = (nextRed[0] + dr[i], nextRed[1] + dc[i])
                redStr = map1[nextRed[0]][nextRed[1]]
            nextRed = (nextRed[0] - dr[i], nextRed[1] - dc[i])

            if not switch:
                map1[nextRed[0]][nextRed[1]] = "R"
            if nextRed != red:
                map1[red[0]][red[1]] = "."

            # 파란공 다시 체크
            if flag == 2:
                blueStr = map1[nrBlue][ncBlue]
                while blueStr != "#" and blueStr != "R":
                    if blueStr == "O":
                        flag = 1
                        break
                    nextBlue = (nextBlue[0] + dr[i], nextBlue[1] + dc[i])
                    blueStr = map1[nextBlue[0]][nextBlue[1]]
                nextBlue = (nextBlue[0] - dr[i], nextBlue[1] - dc[i])
                if flag == 1: 
                    switch = 0
                    map1[red[0]][red[1]] = "R"
                    if nextRed != red:
                        map1[nextRed[0]][nextRed[1]] = "."
                    continue

            if switch == 1:
                print(1)
                exit()
            
            map1[nextBlue[0]][nextBlue[1]] = "B"
            if nextBlue != blue:
                map1[blue[0]][blue[1]] = "."
            visited.add((nextRed, nextBlue))

            # for i in map1:
            #     print(*i)
            # print()

            back(nextRed, nextBlue, cnt + 1)
            
            map1[nextRed[0]][nextRed[1]] = "."
            map1[red[0]][red[1]] = "R"
            map1[nextBlue[0]][nextBlue[1]] = "."
            map1[blue[0]][blue[1]] = "B"
            visited.discard((nextRed, nextBlue))

back(startRed, startBlue, 0)

print(0)


# if sol == float('inf'):
#     print(0)
            