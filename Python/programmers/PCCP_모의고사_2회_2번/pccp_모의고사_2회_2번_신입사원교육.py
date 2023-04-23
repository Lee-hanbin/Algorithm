# pccp_모의고사_2회_2번_신입사원교육

from heapq import heapify, heappush, heappop

def solution(ability, number):
    heapify(ability)
    for _ in range(number):
        a = heappop(ability)
        b = heappop(ability)
        tmp = a + b
        heappush(ability, tmp)
        heappush(ability, tmp)
        
    answer = sum(ability)
    return answer