# BOJ_24508_silver1-나도리팡

import sys

input = sys.stdin.readline

N, K, T = map(int, input().split())

box = sorted(list(map(int, input().split())))

s, e = 0, N-1
while T > 0 and s < e:
    l = box[s]
    r = box[e]
    tmp = l + r
     
    # 시작값과 끝값의 합이 최대 바구니보다 큰 경우
    if tmp > K:
        gab = K - r
        box[s] -= gab
        box[e] = 0
        T -= gab
        e -= 1
    # 시작값과 끝값의 합이 최대 바구니 크기와 같은 경우
    elif tmp == K:
        box[s], box[e] = 0, 0
        T -= l
        s += 1
        e -= 1
    # 시작값과 끝값의 합이 최대 바구니보다 작은 경우
    else:
        box[e] += l
        box[s] = 0
        T -= l
        s += 1

if sum(box) < 1 and T > -1:
    print("YES")
else:
    print("NO")