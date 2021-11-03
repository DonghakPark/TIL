from collections import deque

a, b = map(int, input().split())
board = []
answer = ""
for i in range(a):
    board.append(list(input()))

# 오른쪽, 아래, 왼쪽, 위쪽
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

start_candidate = []

for x in range(a):
    for y in range(b):
        count = 0
        if board[x][y] == "#":
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < a and 0 <= ny < b and board[nx][ny] == "#":
                    count += 1

            start_candidate.append([count, x,y])

start_candidate.sort()
_, start_x, start_y = start_candidate[0]
start_d = 0

for i in range(4):
    nx = start_x + dx[i]
    ny = start_y + dy[i]
    if 0 <= nx < a and 0 <= ny < b and board[nx][ny] == "#":
        start_d = i
        break

print(start_x + 1, start_y + 1)
print_d = [">", "v", "<", "^"]
print(print_d[start_d])

Q = deque()
Q.append([start_x, start_y, start_d])

visited = [[0] * b for _ in range(a)]
visited[start_x][start_y] = 1

while Q:
    now_x, now_y, now_d = Q.popleft()

    nx = now_x + (dx[now_d])
    ny = now_y + (dy[now_d])
    nx_2 = now_x + (dx[now_d] * 2)
    ny_2 = now_y + (dy[now_d] * 2)
    if 0 <= nx < a and 0 <= ny < b and board[nx][ny] == "#" and board[nx_2][ny_2] == "#":
        if visited[nx][ny] == 0 and visited[nx_2][ny_2] == 0:
            Q.append([nx_2, ny_2, now_d])
            answer += "A"
            visited[nx][ny] = 1
            visited[nx_2][ny_2] = 1
            continue

    right_d = (now_d + 1) % 4
    nx = now_x + (dx[right_d])
    ny = now_y + (dy[right_d])
    nx_2 = now_x + (dx[right_d] * 2)
    ny_2 = now_y + (dy[right_d] * 2)
    if 0 <= nx < a and 0 <= ny < b and board[nx][ny] == "#" and board[nx_2][ny_2] == "#":
        if visited[nx][ny] == 0 and visited[nx_2][ny_2] == 0:
            Q.append([nx_2, ny_2, right_d])
            answer += "RA"
            visited[nx][ny] = 1
            visited[nx_2][ny_2] = 1
            continue

    left_d = (now_d - 1) % 4
    nx = now_x + (dx[left_d])
    ny = now_y + (dy[left_d])
    nx_2 = now_x + (dx[left_d] * 2)
    ny_2 = now_y + (dy[left_d] * 2)
    if 0 <= nx < a and 0 <= ny < b and board[nx][ny] == "#" and board[nx_2][ny_2] == "#":
        if visited[nx][ny] == 0 and visited[nx_2][ny_2] == 0:
            Q.append([nx_2, ny_2, left_d])
            answer += "LA"
            visited[nx][ny] = 1
            visited[nx_2][ny_2] = 1
            continue

print(answer)