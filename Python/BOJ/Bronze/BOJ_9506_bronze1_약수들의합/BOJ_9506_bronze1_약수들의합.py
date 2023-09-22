# BOJ_9506_bronze1_약수들의합
import sys
input = sys.stdin.readline

for i in sys.stdin:
    i = int(i)
    if i < 0:
        break
    
    chk_lst = []
    for j in range(1, i):
        if not i%j:
            chk_lst.append(j)
    if sum(chk_lst) == i:
        print(str(i) + ' =',end=' ' )
        for e in chk_lst[:-1]:
            print(str(e) + ' + ',end='')
        print(str(chk_lst[-1]))
    else:
        print(str(i) + ' is NOT perfect.')