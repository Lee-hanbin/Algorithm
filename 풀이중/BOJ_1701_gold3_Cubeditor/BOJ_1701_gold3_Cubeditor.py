# BOJ_1701_gold3_Cubeditor

T = input().strip()
l = len(T)
k = 0
while k < l: 
    for i in range(k+1):
        chk = T[i:l-k+i]
        print(chk)
    k += 1
