# BOJ_9519_gold5-졸려

import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

tmp = s[1:]
length = len(tmp)
dp = []

i = 0

# 몇번 돌아야 순회하는지 찾는 반복문
while 1:
    left = ""
    for j in range(length//2):
        left += tmp[length - j - 1]
        left += tmp[j]

    if length % 2:      # 기존 문자가 짝수이면 중간 문자를 마지막에 추가
        tmp = left + tmp[length//2]
    else:               # 기존 문자가 홀수
        tmp = left

    dp.append(s[0]+tmp)

    # 처음 문자와 동일하면 해당 문자의 인덱스를 저장하고 반복문을 빠져나옴
    if dp[-1] == s:
        idx = i + 1
        break
    i += 1


# 입력 받은 문자가 실행 후, 문자이므로 뒤로 돌림
idx = -1 * (n % idx) - 1
print(dp[idx])
