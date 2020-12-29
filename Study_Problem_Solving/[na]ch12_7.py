"""
치킨 배달 문제
author : donghak park
contact : donghark03@naver.com
"""

from itertools import combinations

N, M = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

def check():
    sum_a = 0

    for i in range(N):
        for j in range(N):

            if arr[i][j] == 1:
                min_dist = 2e9

                for x in range(N):
                    for y in range(N):
                        if arr[x][y] == 2:
                            dist = abs(i -x) + abs(j-y)
                            min_dist = min(dist, min_dist)

                sum_a += min_dist
    return sum_a

candidate = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            candidate.append([i,j])
            arr[i][j] = 0

test = list(combinations(candidate, M))
answer = 2e9

for element in test:
    for x,y in element:
        arr[x][y] = 2
    answer = min(answer, check())
    for x,y in element:
        arr[x][y] = 0

print(answer)