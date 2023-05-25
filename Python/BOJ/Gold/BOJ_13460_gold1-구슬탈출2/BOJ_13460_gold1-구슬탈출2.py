# BOJ_13460_gold1-구슬탈출2

import sys
input = sys.stdin.readline


n, m = map(int, input().split())

map1 = list(list(input().rstrip()) for _ in range(n))

for i in map1:
    print(*i)

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
            redStr, blueStr = map1[nrRed][ncRed], map1[nrBlue][ncBlue]
            nextRed, nextBlue = (nrRed, ncRed), (nrBlue, ncBlue)
            while redStr != "#":
                if redStr == "O":
                    break
                nextRed = (nrRed[0] + dr[i], ncRed[1] + ncRed[i])
                redStr = map1[nextRed[0]][nextRed[1]]

            while blueStr != "#":
                if blueStr == "O":
                    break
                nextBlue = (nrBlue[0] + dr[i], ncBlue[1] + ncBlue[i])
                blueStr = map1[nextBlue[0]][nextBlue[1]]

                continue

            if redStr == "#":
                nextRed = red
            if blueStr == "#":
                nextBlue = blue
            if blueStr == "O":
                continue
            else:                
                if redStr == "O":
                    # sol = min(cnt, sol)
                    print(1)
                    exit()
                if nextRed == nextBlue:
                    continue
                else:
                    visited.add((nextRed, nextBlue))
                    back(nextRed, nextBlue, cnt + 1)
                    visited.discard((nextRed, nextBlue))

back(startRed, startBlue, 0)

if sol == float('inf'):
    print(0)
            