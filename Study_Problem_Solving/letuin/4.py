dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def find_route(x, y, d, count):
    global answer
    if x == N-1 and y == N-1:
        answer = count
        return

    nd = (d-1) % 4
    while True:
        nx, ny = x + dx[nd], y + dy[nd]
        if 0<= nx < N and 0 <= ny <N and Arr[nx][ny] != 1:
            find_route(nx,ny,nd,count+1)
            break

        else:
            nd = (nd + 1) % 4


N = int(input())
Arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0

find_route(0, 0, 1, 0)
print(answer)
