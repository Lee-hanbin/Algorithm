# PCCP_모의고사_1회_4번 운영체제

from heapq import heappop, heappush

# [[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]

program = [[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]


# b에 의해서 프로그램 실행여부가 정해지므로 (시간순서대로임!!)
# b에 대해서 내림차순으로 정렬한다.
program.sort(key=lambda x: -x[1])
q = []
answer = [0] * 11
t = 0 

# 프로그램을 모두 돌리고 큐가 빌때까지 반복한다.
while program or q:
    # 큐가 비어있으면 전체 대기 시간을 할당한다. (초기값)
    if not q:
        answer[0] = program[-1][1]
    # 큐에 값이 있으면 하나를 빼서 
    # 해당 인덱스에 총 진행 시간 - 실행시간으로 갱신
    else:
        a, b, c = heappop(q)
        answer[a] += answer[0] - b
        answer[0] += c

    # 프로그램이 남아 있고 프로그램의 실행 시각이 
    # 총 진행 시간보다 작거나 같으면 program을 힙큐에 넣는다 
    while program and program[-1][1] <= answer[0]:
        heappush(q, program.pop())        

print(*answer)