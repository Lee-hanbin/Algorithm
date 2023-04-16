# BOJ_1701_gold3_Cubeditor

import sys
input = sys.stdin.readline

def pre_process(P):
    next = [0] * len(P)
    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = next[j-1]
        if P[i] == P[j]:
            next[i] = j + 1
            j += 1
    return next
ans = 0
string = input().strip()
l = len(string)
for i in range(l):
    ans = max(ans, max(pre_process(string[i:])))

print(ans)