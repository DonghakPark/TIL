#치킨 배달

from itertools import combinations

N, M = map(int, input().split())

ori = []

for _ in range(N):
    ori.append(list(map(int, input().split())))

home = []
store = []

for i in range(N):
    for j in range(N):
        if ori[i][j] == 1:
            home.append([i+1, j+1])
        elif ori[i][j] == 2:
            store.append([i+1,j+1])

def calculate(home, store):
    chi_dis = 0

    for x, y in home:
        dist = 1e9
        for x_2, y_2 in store:
            temp = abs(x - x_2) + abs(y - y_2)
            dist = min(temp, dist)
        chi_dis += dist

    return chi_dis

combi = list(combinations(store, M))
result = 1e9

for case in combi:
    case = list(case)

    temp = calculate(home, case)
    result = min(temp, result)

print(result)