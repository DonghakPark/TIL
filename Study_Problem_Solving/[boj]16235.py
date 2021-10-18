"""
나무 재테크 문제
Author : donghak park
"""

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

N, M, K = map(int, input().split())

ground = [list(map(int, input().split())) for _ in range(N)]
back_ground = [[5] * N for _ in range(N)]

tree = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

year = 0

while year < K:


    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                tree[i][j].sort()

                temp = []
                dead = 0

                for element in tree[i][j]:
                    if element <= back_ground[i][j]:
                        back_ground[i][j] -= element
                        temp.append(element+1)
                    else:
                        dead += element // 2
                back_ground[i][j] += dead
                tree[i][j] = []
                tree[i][j].extend(temp)

    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                for element in tree[i][j]:
                    if element % 5 == 0:
                        for d in range(8):
                            nx = i + dx[d]
                            ny = j + dy[d]
                            if 0 <= nx < N and 0 <= ny < N:
                                tree[nx][ny].append(1)

    for i in range(N):
        for j in range(N):
            back_ground[i][j] += ground[i][j]

    year += 1

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree[i][j])

print(answer)