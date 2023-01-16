# BOJ_1599_gold5-민식어

import sys
input = sys.stdin.readline

lst =       ['a', 'b', 'k', 'd', 'e', 'g', 'h', 'i', 'l', 'm', 'n', 'ng', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y']
lst_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
sort_dict = dict()

for i, e in enumerate(lst):
    sort_dict[e] = i

n = int(input())
str_lst = [input().rstrip() for _ in range(n)]
cnt_lst = [''] * n

# 문자의 알파벳화
for i, s in enumerate(str_lst):
    for idx, alpha in enumerate(s):
        if idx > 0 and alpha == 'g' and s[idx-1] == 'n':            # ng로 처리된 g이면 pass
            continue
        if idx + 1 < len(s) and alpha == 'n' and s[idx+1] == 'g':   # ng가 연속되게 오면 ng로 변경
            alpha = 'ng'           
        cnt_lst[i] += lst_alpha[sort_dict[alpha]]                   # 민식어를 알파벳으로 변경
    cnt_lst[i] = (cnt_lst[i], i)                                    # 민식어로 돌아갈 수 있게 인덱스 추가

# 알파벳으로 변환 후, 정렬 
cnt_lst.sort(key = lambda x: x[0])

# 정렬된 문자 출력
for i in cnt_lst:
    idx = i[1]
    print(str_lst[idx])
