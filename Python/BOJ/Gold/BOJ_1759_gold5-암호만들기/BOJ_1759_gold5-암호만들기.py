# BOJ_1759_gold5-암호만들기

import sys
from itertools import combinations

input = sys.stdin.readline

L, C = map(int, input().split())

vowels_set = {"a", "e", "i", "o", "u"}
consonants_lst = []
vowels_lst = []

# 모음 자음 나누기
for alpha in list(input().split()):
    if alpha in vowels_set:
        vowels_lst.append(alpha)
        continue
    consonants_lst.append(alpha)

sol = []

# 모음 1개부터 L-2개 까지
for i in range(1, L-1):
    # 모음 뽑기
    for vow in combinations(vowels_lst, i):
        tmp1 = list(vow)
        # 자음 뽑기
        for con in combinations(consonants_lst, L-i):
            tmp2 = list(con)
            tmp3 = tmp2 + tmp1
            tmp3.sort()             # 문자열 오름차순
            sol.append(tmp3)

sol.sort()      # 사전식 출력

for i in sol:
    print(''.join(i))