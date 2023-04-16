# BOJ_2302_silver1-극장좌석

import sys

def chk_fnc(k):
    if k == 1 or k == 0:
        return 1
    if k == 2:
        return 2
    dp = [0] * (k+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, k+1):
       dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]

n = int(input().strip())
m = int(input().strip())
# if n == 1 and m == 1 or n == 2 and m == 1:
#     print(1)
#     exit()

lst = list(range(1,n+1))
vip_lst = []
lst_partition = []
if m > 0:
    for i in range(m):
        vip_lst.append(int(input().strip()))
    j = 0
    for i in vip_lst:
        lst_partition.append(lst[j:i-1])
        j = i
    lst_partition.append(lst[j:])
else:
    lst_partition.append(lst)
# print(lst_partition)

sol = 1
for i in lst_partition:
    k = len(i)
    sol *= chk_fnc(k)
print(sol)