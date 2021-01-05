"""
금광 문제
author : donghak park
contact : donghark03@naver.com
"""

T = int(input())

dx = [-1,0,1]
dy = [-1,-1,-1]

for test_case in range(T):
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))

    arr = []
    visited = [[0] * M for _ in range(N)]

    for i in range(N):
        arr.append(temp[i*M:(i+1)*M])

    for i in range(N):
        visited[i][0] = arr[i][0]

    for y in range(1, M):
        for x in range(N):
            temp = []
            for i in range(3):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and ny >= 0 and nx <N and ny < M:
                    temp.append(visited[nx][ny])
            visited[x][y] = max(temp) + arr[x][y]

    answer = []
    for i in range(N):
        answer.append(visited[i][M-1])

    answer.sort()
    print(answer[-1])

