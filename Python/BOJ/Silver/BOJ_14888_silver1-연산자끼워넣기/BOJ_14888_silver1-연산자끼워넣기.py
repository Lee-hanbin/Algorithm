# BOJ_14888_silver1-연산자끼워넣기

#dfs 풀이

N = int(input())
lst = list(map(int,input().split()))
a, s, m, d = map(int, input().split())

max_value = -1e9
min_value = 1e9

def dfs(i, now):
    global min_value, max_value, a, s, m, d
    if i == N:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if a > 0:
            a -= 1
            dfs(i+1, now+lst[i])
            a += 1
        if s > 0:
            s -= 1
            dfs(i+1, now-lst[i])
            s += 1
        if m > 0:
            m -= 1
            dfs(i+1, now*lst[i])
            m += 1
        if d > 0:
            d -= 1
            dfs(i+1, int(now/lst[i]))
            d += 1

dfs(1, lst[0])

print(max_value)
print(min_value)