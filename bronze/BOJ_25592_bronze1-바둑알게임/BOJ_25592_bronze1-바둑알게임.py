# BOJ_25592_bronze1-바둑알게임

n = int(input())


puang = 0
you = 0
i = 0
while n > 0:
    i += 1
    if i % 2:
        puang += i
    else:
        you += i
    n -= i

# print(puang)
# print(you)
# print(i)
# print(n)
if i % 2:       # i가 홀수
    if n < 0:
        print(n*-1)
    else:
        print(0)

else:           # i가 짝수
    if n < 0:
        print(0)
    else:
        print(i+1)