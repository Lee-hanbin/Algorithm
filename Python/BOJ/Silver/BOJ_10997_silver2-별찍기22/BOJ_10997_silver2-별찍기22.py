# BOJ_10997_silver2-별찍기22

import sys

input = sys.stdin.readline

n = int(input())

dp = [''] * 101
dp[1] = ['*']
dp[2] = [
    '*****',
    '*    ',
    '* ***',
    '* * *',
    '* * *',
    '*   *',
    '*****'
]
    
# 1, 5, 9, 13
for i in range(3, n+1):
    m = 4 * i - 3 
    up = ['*' * m, '*' + ' ' * (m-1)]                  # 위에 뚜껑 추가
    for j in range(m - 2):                                      # 중간부분 앞 뒤 추가
        if j == 0:
            dp[i-1][j] = '* ' + dp[i-1][j] + '**'
        else:
            dp[i-1][j] = '* ' + dp[i-1][j] + ' *'
    down = ['*'+ ' ' * (m-2) + '*', '*' * m]        # 아래 바닥  추가
    dp[i] = up + dp[i-1] + down


for i in dp[n]:
    print(i.rstrip())


# BOJ_10997_silver2-별찍기22

dp = [''] * 101
dp[1] = ['*']
dp[2] = [
    ['*', '*', '*', '*', '*'],
    ['*', ' ', ' ', ' ', ' '],
    ['*', ' ', '*', '*', '*'],
    ['*', ' ', '*', ' ', '*'],
    ['*', ' ', '*', ' ', '*'],
    ['*', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*'],
]

for i in range(3, n+1):
    m = 4 * i - 3 
    up = [['*'] * m] + [['*'] + [' '] * (m-1)]
    for j in range(m - 2):
        if j == 0:
            dp[i-1][j] = ['*', ' '] + dp[i-1][j] + ['*', '*'] 
        else:
            dp[i-1][j] = ['*', ' '] + dp[i-1][j] + [' ', '*']
    down = [['*']+ [' '] * (m-2) + ['*']] +  [['*'] * m]
    dp[i] = up + dp[i-1] + down


for i in dp[n]:
    print(''.join(i).rstrip())
