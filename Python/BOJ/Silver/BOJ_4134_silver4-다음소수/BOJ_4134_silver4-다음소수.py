# BOJ_4134_silver4-다음소수

import sys
input = sys.stdin.readline


# 소수판별함수
def is_prime_number(n):

    # 0과 1인 경우는 다음 수로
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+ 1):
        if not n % i:
            return False
    return True


N = int(input())
lst2 = [int(input()) for i in range(N)]

for i in lst2:
    n = i

    #소수가 맞을때까지 돌리기
    while not is_prime_number(n):
            n += 1

    print(n)    

    