# BOJ_10859_silver2-뒤집혀진소수

import sys

input = sys.stdin.readline

def is_prime_number(n):
    for i in range(2, int(n**0.5)+ 1):
        if n % i == 0:
            return False
    return True

befor_n = int(input())

n = list(str(befor_n))
n_chk = set(n)

if befor_n == 1:
    print('no')
    exit()

if '3' in n_chk or '4' in n_chk or '7' in n_chk:
    print('no')
    exit()

if is_prime_number(befor_n):
    change_n = ''
    while n:
        num = n.pop()
        if num in ['0', '1', '2', '5', '8']:
            change_n += num
        elif num == '6':
            change_n += '9'
        elif num == '9':
            change_n += '6'
        else:
            print('no')
            break
    else:
        if is_prime_number(int(change_n)):
            print('yes')
        else:
            print('no')
else:
    print('no')


        