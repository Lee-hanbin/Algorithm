# BOJ_24060_silver4-알고리즘수업-병합정렬1

import sys
input = sys.stdin.readline

def merge_sort(lst, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(lst,p,q)
        merge_sort(lst,q+1,r)
        merge(lst,p,q,r)

def merge(chk_lst, p, q, r):
    global sol, cnt, K
    tmp = []
    i = p
    j = q + 1
    while i<=q and j<=r:
        if chk_lst[i] <= chk_lst[j]:
            tmp.append(chk_lst[i])
            i += 1
        else:
            tmp.append(chk_lst[j])
            j += 1

    while i <= q:
        tmp.append(chk_lst[i])
        i += 1

    while j <= r:
        tmp.append(chk_lst[j])
        j += 1

    i = p
    t = 0
    while i <= r:
        cnt += 1
        if cnt == K:
            sol = tmp[t]
        chk_lst[i] = tmp[t]
        i += 1
        t += 1
        # print(chk_lst)


N, K = map(int, input().split())
lst= list(map(int,input().split()))
sol = -1 
cnt = 0
merge_sort(lst,0, N-1)
print(sol)