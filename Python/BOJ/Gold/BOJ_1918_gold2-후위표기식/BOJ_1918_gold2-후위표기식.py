import sys

input = sys.stdin.readline

n = list(input().rstrip())

# 연산자의 우선순위를 dict형태로 저장
oper_dict = {
    '+' : 1,
    '-' : 1, 
    '*' : 2, 
    '/' : 2, 
    '(' : 0,
    ')' : 0
    }

postfix = ''
operator_stack = []

for i in n:
    # 문자이면 스택에 넣기
    if i not in oper_dict.keys():
        postfix += i

    # 열린 괄호면 스택에 넣기
    elif i == '(':
        operator_stack.append(i)

    # 닫힌 괄호면 스택에 열린 괄호가 나올 때까지 POP
    elif i == ')':
        while 1:
            pre = operator_stack.pop()
            if pre == '(':
                break
            else:
                postfix += pre
        # operator_stack.pop()
    else:
        # 현재 연산자가 스택의 top 연산자보다 우선순위가 높은 경우
        while operator_stack and oper_dict[i] <= oper_dict[operator_stack[-1]]:
            postfix += operator_stack.pop()
        # 그렇지 않은 경우거나 낮은 우선순위를 가진 연산자를 모두 pop한 경우
        operator_stack.append(i)
        
# 항상 연산자 스택에는 하나 이상의 연산자가 존재하므로 스택을 비워준다
while operator_stack:
    postfix += operator_stack.pop()
    
print(postfix)