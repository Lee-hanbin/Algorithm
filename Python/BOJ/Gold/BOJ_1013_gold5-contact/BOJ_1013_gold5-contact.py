# BOJ_1013_gold5-contact

import sys

input = sys.stdin.readline


# 10000110001

'''
1 => 1001 100001 100000 01 => 100로 시작했으면 1로 끝나야함 
  => 1100 11100 111100     => 11로 시작했으면 100으로 끝나야함
0 => 01 => 01
'''

def dfs(cnt):
    global chk
    if cnt > length:
        return
    if cnt == length:
        chk = 'YES'
        return 
    
    if s[cnt] == '1':
        if cnt+3 < length and s[cnt:cnt+3] == '100':
            cnt += 3
            while cnt < length and s[cnt] == '0':
                cnt += 1
            dfs(cnt + 1)
        elif cnt+1 < length and s[cnt:cnt+2] == '11':
            cnt += 2

            while cnt < length:
                print('zzz')
                if cnt + 3 < length and s[cnt:cnt+3] =='100':
                    cnt += 2
                    break
                if cnt + 1 < length and s[cnt+1] =='1':
                    cnt += 1
            dfs(cnt+1)
    else:
        if cnt + 1 < length and s[cnt:cnt+2] == '01':
            dfs(cnt + 2)

n = int(input())

for _ in range(n):
    s = input().rstrip()
    length = len(s)
    chk = 'NO'
    
    dfs(0)

    print(chk)

# 10011000111
# 100111001


# import sys
# input = sys.stdin.readline

# def dfs(i, end):
# 	result = 0
# 	if i == end:
# 		return i
# 	if pattern[i:i + 2] == "01":
# 		if i + 2 == end:
# 			return i + 2
# 		else:
# 			result = max(result, dfs(i + 2, end))
# 	elif i + 4 <= end and pattern[i:i + 2] == "10":
# 		i += 2
# 		if pattern[i] != '0':
# 			return 0
# 		while pattern[i] == '0':
# 			i += 1
# 			if i == end:
# 				return 0
# 		while pattern[i] == "1":
# 			result = max(dfs(i + 1, end), result)
# 			i += 1
# 			if i == end:
# 				return i
# 	return result

# N = int(input())
# for _ in range(N):
# 	pattern = input().rstrip()
# 	if dfs(0, len(pattern)) == len(pattern):
# 		print("YES")
# 	else:
# 		print("NO")