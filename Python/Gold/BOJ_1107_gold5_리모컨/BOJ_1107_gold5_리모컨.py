# BOJ_1107_gold5_리모컨

import sys
input = sys.stdin.readline

# 기본 연산
def operator1(find, find_length, sol, sol_num):
    # 맞는 버튼이 없을 때, 가장 가까운 버튼 고르기
    button_copy = button[::]
    for i in range(len(button)):
        button_copy[i] -= int(find[sol])
        button_copy[i] = abs(button_copy[i])
    idx = button_copy.index(min(button_copy))
    tmp = button[idx]

    # 제일 큰 자리수가 변경되는 경우
    if button[idx] != button[-1] and len(button)>1:
        # 원래 숫자와 근접한 버튼의 차이가 동일한 경우
        if abs(int(find[sol]) - button[idx]) == abs(int(find[sol]) - button[idx + 1]) :
            # 자릿 수의 숫자를 하나 올렸을 때 차이가 더 적은 경우
            if sol+1 < find_length and abs(int(find[sol+1]) - button[0] - 10) < abs(10 + int(find[sol+1]) - button[-1]):
                tmp = button[idx+1]

    sol_num += str(tmp)
    sol += 1

    # 없는 버튼 중에 근접한 버튼 고르기
    if tmp > int(find[sol-1]):  # 버튼이 원하는 숫자보다 클때
        for i in range(sol, find_length):
            sol_num += str(button[0])
            sol += 1
    else:                       # 버튼이 원하는 숫자보다 작을때
        for i in range(sol, find_length):
            sol_num += str(button[-1])
            sol += 1
    
    return abs(int(find)- int(sol_num)) + sol


# 자릿수를 하나 내리기
def operator2(find, find_length, sol, sol_num):
    tmp_str = str()
    # 버튼이 일부 눌려있는 경우
    if sol_num:
        # 버튼이 눌린 마지막 자리의 숫자를 하나 지우고
        idx = button.index(int(sol_num[-1])) - 1
        # 버튼이 하나만 눌린 경우, 자리수를 하나 내리고 가장 큰 값
        if idx < 0:
            find_length -= 1
            for i in range(find_length):
                tmp_str += str(button[-1])
        # 버튼이 하나 이상 눌린 경우, 버튼이 눌린 마지막 자리수의 숫자를 한칸 내리고 나머지는 가장 큰 값
        else:
            sol_num = list(sol_num)
            sol_num[-1] = button[idx]
            for i in sol_num:
                tmp_str += str(i)
            for i in range(sol, find_length):
                tmp_str += str(button[-1])
    # 버튼이 하나도 안 눌려있는 경우
    else:
        for i in range(find_length-1):
            tmp_str += str(button[-1])
        find_length -= 1
    if tmp_str:
        tmp_str = int(tmp_str)
    else:
        tmp_str = float('inf')
    return abs(int(find) - tmp_str) + find_length


# 자릿수를 하나 올리기
def operator3(find, find_length, sol, sol_num):
    tmp_str = str()
    # 버튼을 눌렀을 때
    if sol_num:
        idx = button.index(int(sol_num[-1])) + 1
        if idx == len(button):
            return float('inf')
        sol_num = list(sol_num)
        sol_num[-1] = button[idx]
        for i in sol_num:
            tmp_str += str(i)
        for i in range(sol, find_length):
            tmp_str += str(button[0])
    # 버튼을 누르지 않았을 때
    else:
        find_length += 1
        for i in range(find_length):
            if i == 0 and button[0] == 0 and len(button) > 1:
                tmp_str += str(button[1])
                continue
            tmp_str += str(button[0])
    return abs(int(find) - int(tmp_str)) + find_length

num = input().rstrip()
n = int(input())
fail = []
if n:
    fail = list(map(int, input().split()))

# 100이 입력되면 0 출력
if num == str(100):
    print(0)
    exit()

if n == 10 or (n == 9 and sum(fail)==45 and int(num) > 50):
    print(abs(int(num)- 100))
else:
    # 가능한 button 구하기
    num_length = len(num)
    button = []
    for i in range(10):
        if i in fail:
            continue
        button.append(i)

    # 가능한 버튼 체크
    rst = 0
    rst_num = str()
    for i in num:
        if int(i) not in button:
            break
        rst_num += str(i)
        rst += 1    
    else:
        print(min(abs(int(num) - 100), rst))
        exit()

    print(min(abs(int(num) - 100), operator1(num, num_length, rst, rst_num), operator2(num, num_length, rst, rst_num), operator3(num, num_length, rst, rst_num)))  




