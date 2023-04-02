from collections import defaultdict

def solution(input_string):
    dict1 = defaultdict()
    check = ""
    alphabet_set = set()
    answer = set()
    for alphabet in input_string:
        if alphabet in alphabet_set:
            if alphabet != check:
                answer.add(alphabet)
                check = alphabet
        else:
            alphabet_set.add(alphabet)
            dict1[alphabet] = 1
            check = alphabet
    if answer:
        answer = sorted(list(answer))
        return ''.join(answer)
    else:
        return "N"
s = input().rstrip()

print(solution(s))