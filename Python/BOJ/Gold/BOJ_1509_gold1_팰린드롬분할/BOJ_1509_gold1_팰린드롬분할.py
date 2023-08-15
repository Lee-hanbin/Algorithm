# BOJ_1509_gold1_팰린드롬분할

import sys

input = sys.stdin.readline

s = ' ' + input().rstrip()
n = len(s) - 1

dp = [[0]*(n+1) for _ in range(n+1)]
res = list(range(n+1))

for i in range(n):
    for k in range(1, n+1-i):
        # 자기 자신은 팰린드롬이므로 초기화
        if not i:
            dp[k][k] = 1
        # 전체를 돌면서 문자의 길이가 2인 팰린드롬 초기화
        elif i==1 and s[k] == s[k+1]:
            dp[k][k+1] = 1
        # 한 글자 늘렸을 때, 초기값과 추가된 값이 동일하고 그 안에 있는 문자열이 팰린드롬이면 팰린드롬
        # ex) ABCBA => C + ABCBA + C => C == C & ABCBA 가 팰린드롬 => 추가했을때, 팰린드롬
        else:
            if s[k] == s[k+i] and dp[k+1][k+i-1]:
                dp[k][k+i] = 1

for i in range(1, n+1):
    res[i] = min(res[i], res[i-1] + 1)
    for j in range(i+1, n+1):
        if dp[i][j]:
            res[j] = min(res[j],res[i-1] + 1)

for i in dp:
    print(*i)
print(res)
print(res[-1])