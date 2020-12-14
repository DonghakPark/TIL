# 뱀 문제

N = int(input())
K = int(input())

apple = []

for _ in range(K):
    apple.append(list(map(int,input().split())))

L = int(input())

dir = []
for _ in range(L):
    X, C = input().split()

    dir.append([int(X), C])

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def move():

    snake = [[1,1]]

    x, y = 1, 1

    len = 1
    head = 0

    time = 0

    while True:

        nx = x + dx[head]
        ny = y + dy[head]

        if nx >= N+1 or nx < 1 or ny >= N+1 or ny < 1 or [nx,ny] in snake:
            return time +1

        time += 1

        if [nx,ny] in apple:
            len += 1
            x = nx
            y = ny
            apple.remove([nx,ny])
            snake.append([nx,ny])
        else:
            snake.pop(0)
            x = nx
            y = ny
            snake.append([x,y])


        if dir:
            if dir[0][0] == time:
                X, C = dir.pop(0)
                if C == "D":
                    head = (head + 1)%4

                elif C == "L":
                    head = (head - 1)%4



print(move())