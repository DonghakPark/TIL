# 연구소 3
import copy
from collections import deque
from itertools import combinations

N, M = map(int, input().split())

lab = []

for _ in range(N):
    lab.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

activate = []

for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            activate.append([i, j])


# 바이러스를 퍼트리는 함수
def virus(x, y):
    Q = deque([])
    Q.append([x, y])
    temp[x][y] = 0
    time = 0

    while Q:
        x1, y1 = Q.popleft()

        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if temp[nx][ny] == -1 and lab[nx][ny] == 0:
                    Q.append([nx, ny])
                    temp[nx][ny] = temp[x1][y1] + 1
                if temp[nx][ny] != -1:
                    if temp[nx][ny] < temp[x][y] + 1:
                        continue
                    else:
                        temp[nx][ny] = temp[x][y] + 1
                if lab[nx][ny] == 2 and ([nx, ny] not in activate):
                    virus(nx, ny)


# 모두 퍼졌는지 체크 True 이면 모두 퍼졌다.
def check():
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 0:
                return False

    return True


def find_max():
    max_ = 0
    for i in range(N):
        for j in range(N):
            if temp[i][j] > max_:
                max_ = temp[i][j]
    return max_


combi = list(combinations(activate, M))

answer = 1e9
flag = False

for element in combi:
    temp = [[-1] * N for _ in range(N)]
    for position in element:
        virus(position[0],position[1])

    if check():
        answer = min(find_max(), answer)
        flag = True
    print(temp)
if flag is False:
    answer = -1
print(answer)
