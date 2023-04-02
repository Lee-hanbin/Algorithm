from collections import defaultdict

def solution(queries):
    answer = []
    pattern = defaultdict()
    pattern["RR"] = ["RR", "RR", "RR", "RR"]
    pattern["rr"] = ["rr", "rr", "rr", "rr"]
    pattern["Rr"] = ["RR", "Rr", "Rr", "rr"]

    for n, p in queries:
        entity = "Rr"
        check_lst = []
        p-=1

        while n > 1:
            chk = p % 4
            check_lst.append(chk)

            p = p // 4 
            n -= 1
        while check_lst:
            entity = pattern[entity][check_lst.pop()]
        # check_lst = check_lst[::-1]
        # for i in check_lst:
        #     entity = pattern[entity][i]
        answer.append(entity)

    return answer

print(solution([[4, 64]]))