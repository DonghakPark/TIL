"""
탈출 문제
Author : DongHak Park
Contact : donghark03@naver.com
"""
import heapq

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def move_water():
    global arr
    target = []

    for i in range(R):
        for j in range(C):
            if arr[i][j] == "*":
                for k in range(4):
                    next_x, next_y = i + dx[k], j + dy[k]
                    if 0 <= next_x < R and 0 <= next_y < C:
                        if arr[next_x][next_y] not in ["X", "D", "*"]:
                            target.append([next_x, next_y])
    for element in target:
        x, y = element
        arr[x][y] = "*"


def find(x, y):
    visited = [[False] * C for _ in range(R)]

    Q = []
    heapq.heappush(Q, [0, x, y])
    visited[x][y] = True
    temp_answer = int(1e9)
    now = 0
    while Q:
        count, now_x, now_y = heapq.heappop(Q)

        if arr[now_x][now_y] == "D":
            temp_answer = min(temp_answer, count)

        if now <= count:
            move_water()
            now += 1

        for i in range(4):
            next_x, next_y = now_x + dx[i], now_y + dy[i]
            if 0 <= next_x < R and 0 <= next_y < C and visited[next_x][next_y] is False:
                if arr[next_x][next_y] in [".", "D"]:
                    heapq.heappush(Q, [count + 1, next_x, next_y])
                    visited[next_x][next_y] = True
    if temp_answer != int(1e9):
        return temp_answer
    else:
        return "KAKTUS"


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
x, y = 0, 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == "S":
            x, y = i, j

print(find(x, y))
