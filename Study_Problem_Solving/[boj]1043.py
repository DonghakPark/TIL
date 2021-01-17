"""
거짓말 문제
author : donghak park
contact: donghark03@naver.com
"""
def check_group():
    global know

    for key in group:
        if len(know.intersection(set(group[key]))) != 0 and visited[key] == 0:
            possible[key] = 0
            visited[key] = 1
            know = know.union(set(group[key]))
            check_group()

N, M = map(int, input().split())

know = set(list(map(int, input().split()))[1:])

group = {}
possible = [1] * M
visited = [0] * M
for i in range(M):
    temp = list(map(int, input().split()))[1:]
    group[i] = temp

    if len(set(temp).intersection(know)) != 0:
        know = know.union(set(temp))

check_group()

print(sum(possible))