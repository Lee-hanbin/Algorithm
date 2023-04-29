# PCCP_모의고서_3회_3번

from collections import deque

def solution(menu, order, k):
    answer = 0
    customer = len(order)
    que = deque()
    i = 0
    time = 0
    
    # 큐에 대기손님이 있거나 들어올 고객이 남아있는 경우
    while que or i < customer:
        # 대기손님이 없으면 시간 압축
        if not que:
            time = (i * k) + menu[order[i]]
            i += 1
        # 대기손님 있으면 주문 시간 추가
        else:
            x = que.popleft()
            time += menu[x]

        # 고객이 남아있고 k초가 지났으면 새로운 대기손님
        while i < customer and i <= ((time - 1) // k):
            que.append(order[i])
            i += 1
        
        answer = max(answer, len(que))
        
    return answer + 1