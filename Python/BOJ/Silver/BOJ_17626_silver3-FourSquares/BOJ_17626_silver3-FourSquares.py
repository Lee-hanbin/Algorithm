# BOJ_17626_silver3-FourSquares

# pypy
# n = int(input())
# dp = [0] * (n+1)

# dp[0] = 0
# dp[1] = 1

# for i in range(2, n+1):
#     m = float('inf')
#     for j in range(1, int(i**0.5)+1):
#         m = min(m, dp[i-j**2])
#     dp[i] = m + 1
# print(dp[n])


# python
def check(n) :
    if (n**0.5).is_integer():
        return 1
    for i in range(1, int(n**0.5)+1):
        if (int(n-i*i)**0.5).is_integer():
             return 2
    for i in range(1, int(n**0.5)+1):
        for j in range(1, int((n-i*i)**0.5)+1):
            if ((n-i*i-j*j)**0.5).is_integer(): 
                return 3
    return 4
 
n = int(input())
print(check(n))