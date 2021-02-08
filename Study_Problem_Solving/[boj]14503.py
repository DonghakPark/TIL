"""
로봇 청소기 문제
author : donghak park
contact: donghark03@naver.com
"""
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution():
    global arr
    result = arr

    answer = 0
    Q = deque()
    Q.append([R, C, D, 0])

    while Q:
        x, y, d, count = Q.popleft()

        if arr[x][y] != 2:
            answer += 1
            arr[x][y] = 2

        nd = (d - 1) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]

        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0:
                Q.append([nx, ny, nd, 0])

            elif arr[nx][ny] == 2 or arr[nx][ny] == 1:
                Q.append([x, y, nd, count + 1])

        if count == 4:
            nx = x - dx[d]
            ny = y - dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1:
                    return answer
                else:
                    Q.append([nx, ny, d, 0])

if __name__ == "__main__":
    N, M = map(int, input().split())

    R, C, D = map(int, input().split())
    # 북, 동, 남, 서

    arr = [list(map(int, input().split())) for _ in range(N)]

    print(solution())


