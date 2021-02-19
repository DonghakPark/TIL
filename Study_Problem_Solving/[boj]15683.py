""""
감시 문제
Author : DongHak Park
Contact : donghark03@naver.com
"""

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def see(arr, i, j, dir_list):
    x, y = i, j

    for direct in dir_list:
        nx, ny = x + dx[direct], y + dy[direct]
        while 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0:
                arr[nx][ny] = -1
                nx, ny = nx + dx[direct], ny + dy[direct]
            elif 0 < arr[nx][ny] < 6 or arr[nx][ny] == -1:
                nx, ny = nx + dx[direct], ny + dy[direct]
            elif arr[nx][ny] == 6:
                break

def DFS(stack, index):
    global answer

    if len(stack) == len(cams):

        arr = [[0 for _ in range(M)] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                arr[i][j] = office[i][j]

        for x,y,element in stack:
            see(arr, x, y, element)

        temp = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    temp += 1

        answer = min(answer, temp)

        return

    x, y, t = cams[index]

    if t == 1:
        direct = [[0],[1],[2],[3]]
    elif t == 2:
        direct = [[0,2], [1,3]]
    elif t == 3:
        direct = [[0,1], [1,2], [2,3], [3,0]]
    elif t == 4:
        direct = [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]
    else:
        direct = [[0, 1, 2, 3]]

    for element in direct:
        stack.append([x, y, element])
        DFS(stack, index + 1)
        stack.remove([x, y, element])


N, M = map(int, input().split())

office = [list(map(int, input().split())) for _ in range(N)]

cams = []
answer = int(1e9)

for i in range(N):
    for j in range(M):
        if 0 < office[i][j] < 6:
            cams.append([i, j, office[i][j]])

DFS([], 0)
print(answer)