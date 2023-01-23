# SWEA_1230_암호문3
import sys
sys.stdin = open('input.txt')

# Insert 함수
def Command_I(x, y, s):
    lst_chk = []
    lst_chk = lst[:x] + s + lst[x:]
    return lst_chk

# Delete 함수
def Command_D(x, y):
    lst_chk = []
    lst_chk = lst[:x] + lst[x+y:]
    return lst_chk

# Add 함수
def Command_A(y, s):
    lst_chk = []
    lst_chk = lst + s
    return lst_chk

for t in range(1,11):
    n = int(input().rstrip())

    lst = list(input().split())
    
    m = int(input().rstrip())

    # pop을 이용하기 위해 역슬라이싱
    command = list(input().split())[::-1]
    while command:
        c = command.pop()
        if c == 'I':
            s = []
            x = int(command.pop())
            y = int(command.pop())
            for i in range(y):              # 받을 숫자만큼 pop해서 append
                s.append(command.pop())
            lst = Command_I(x, y, s)
        elif c == 'D':
            x = int(command.pop())
            y = int(command.pop())
            lst = Command_D(x, y)
        else:
            s = []
            y = int(command.pop())
            for i in range(y):              # 받을 숫자만큼 pop해서 append
                s.append(command.pop())
            lst = Command_A(y, s)
    print(f'#{t}',*lst[:10])