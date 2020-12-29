"""
뱀 문제
author : donghak park
contact : donghark03@naver.com
"""

N = int(input())
K = int(input())

board = [[0] * N for _ in range(N)]

for _ in range(K):
    # 첫번째는 행, 두번째는 열
    r, c = map(int, input().split())
    board[r-1][c-1] = 2

L = int(input())
snake = []

for _ in range(L):
    snake.append(input().split())

#### 입력부 끝 #####

x,y = 0, 0

snake_direction = 0

tail = []
tail.append([0,0])

dx = [0,1,0,-1]
dy = [1,0,-1,0]

board[0][0] = 1
time = 0

while True:
    if len(snake) != 0:
        if time == int(snake[0][0]):
            D = snake.pop(0)[1]
            if D == "D":
                snake_direction = ( snake_direction + 1 ) % 4
            else:
                snake_direction = (snake_direction - 1) % 4

    nx = x + dx[snake_direction]
    ny = y + dy[snake_direction]

    if nx < 0 or ny < 0 or nx >= N or ny >= N or board[nx][ny] == 1:
        time += 1
        break
    else:
        if board[nx][ny] == 2:
            board[nx][ny] = 1
            tail.append([nx, ny])
        else:
            t_x, t_y = tail.pop(0)
            board[t_x][t_y] = 0
            board[nx][ny] = 1
            tail.append([nx,ny])
    x,y = nx, ny

    time += 1

print(time)