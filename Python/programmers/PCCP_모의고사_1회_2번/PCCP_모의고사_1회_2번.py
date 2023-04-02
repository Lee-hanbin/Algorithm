answer = 0

def dfs(cnt, power, ability, menu, visited):
    global answer
    if cnt == menu:
        answer = max(answer, power)
        return

    for i, e in enumerate(ability[cnt]):
        if not visited[i]:
            visited[i] = 1
            dfs(cnt + 1, power + e, ability, menu, visited)
            visited[i] = 0


def solution(ability):
    global answer, visited
    menu = len(ability[0])
    ability_tr = []
    visited = [0] * len(ability)

    for i in zip(*ability):
        ability_tr.append(list(i))

    for i, e in enumerate(ability_tr[0]):
       visited[i] = 1
       dfs(1, e, ability_tr, menu, visited)
       visited[i] = 0

    return answer

print(solution([list(map(int, input().split())) for _ in range(5)]))