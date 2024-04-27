# BOJ-1978_silver5-소수찾기

import sys
input = sys.stdin.readline

n = int(input())

stack = []

for i in range(n):
    lst = list(map(int, input().split()))

    if (len(lst) > 1):
        stack.append(lst[1])
    else:
        cmd = lst[0]
        length = len(stack)
        if cmd == 2:
            if length:
                print(stack.pop())
            else:
                print(-1)
        elif cmd == 3:
            print(length)
        elif cmd == 4:
            if length:
                print(0)
            else:
                print(1)
        else:
            if length:
                print(stack[-1])
            else:
                print(-1)

            