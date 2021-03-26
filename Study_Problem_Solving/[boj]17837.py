"""
새로운 게임 2 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def move(now_num):
    global horse

    now_x, now_y, now_d = horse[now_num]

    nx, ny, nd = now_x + dx[now_d], now_y + dy[now_d], now_d
    if nx < 0 or nx >= N or ny < 0 or ny >= N or chess_map[nx][ny] == 2:
        if 0 <= nd <= 1:
            nd = (nd + 1) % 2
        else:
            nd = (nd - 1) % 2 + 2
        nx, ny = now_x + dx[nd], now_y + dy[nd]
        horse[now_num][2] = nd

        if not (0 <= nx < N) or not (0 <= ny < N) or chess_map[nx][ny] == 2:
            return False

    if chess_map[nx][ny] == 0:
        index = chess_map_horse[now_x][now_y].index(now_num)
        new_arr = chess_map_horse[now_x][now_y][index:]

        chess_map_horse[nx][ny] += new_arr

        if new_arr:
            for child in new_arr:
                horse[child][0], horse[child][1] = nx, ny

        chess_map_horse[now_x][now_y] = chess_map_horse[now_x][now_y][:index]
        horse[now_num] = [nx, ny, nd]

    elif chess_map[nx][ny] == 1:
        index = chess_map_horse[now_x][now_y].index(now_num)
        new_arr = chess_map_horse[now_x][now_y][index:]
        chess_map_horse[nx][ny] += new_arr[::-1]

        if new_arr:
            for child in new_arr:
                horse[child][0], horse[child][1] = nx, ny

        chess_map_horse[now_x][now_y] = chess_map_horse[now_x][now_y][:index]
        horse[now_num] = [nx, ny, nd]

    return check_end()


def check_end():
    for i in range(N):
        for j in range(N):
            if len(chess_map_horse[i][j]) >= 4:
                return True
    return False


N, K = map(int, input().split())

chess_map = [list(map(int, input().split())) for _ in range(N)]
chess_map_horse = [[[] for _ in range(N)] for _ in range(N)]
horse = []
for i in range(K):
    x, y, d = map(int, input().split())
    horse.append([x - 1, y - 1, d - 1])
    chess_map_horse[x - 1][y - 1].append(i)

time = 0
flag = False
while True:

    if time > 1000:
        time = -1
        break
    if flag is True:
        break
    time += 1
    for i in range(K):
        if move(i):
            flag = True
            break

print(time)

"""
너무 복잡하게 풀었음
def move_horse(horse_num):
    now_x, now_y, now_d = chess_horse[horse_num]

    next_x, next_y = now_x + dx[now_d], now_y + dy[now_d]

    # 파란색인 경우 or 범위를 벗어나는 경우
    if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N or chess_map[next_x][next_y] == 2:
        next_x, next_y, next_d = 0, 0, 0
        if now_d == 0:
            next_x, next_y, next_d = now_x + dx[1], now_y + dy[1], 1
        elif now_d == 1:
            next_x, next_y, next_d = now_x + dx[0], now_y + dy[0], 0
        elif now_d == 2:
            next_x, next_y, next_d = now_x + dx[3], now_y + dy[3], 3
        elif now_d == 3:
            next_x, next_y, next_d = now_x + dx[2], now_y + dy[2], 2

        if 0 <= next_x < N and 0 <= next_y < N and chess_map[next_x][next_y] != 2:
            chess_horse[horse_num][0], chess_horse[horse_num][1], chess_horse[horse_num][2] = next_x, next_y, next_d

    # 흰색일 경우 이동
    elif chess_map[next_x][next_y] == 0:
        # 이 자리에 이미 말이 있는지 체크
        for i in range(1, K + 1):
            if i == horse_num:
                continue
            if chess_horse[i][0] == next_x and chess_horse[i][1] == next_y:
                horse_child[i].append(horse_num)
                if horse_child[horse_num]:
                    horse_child[i] = horse_child[i] + horse_child[horse_num]

        chess_horse[horse_num][0], chess_horse[horse_num][1], chess_horse[horse_num][2] = next_x, next_y, now_d

    # 빨간색인 경우
    elif chess_map[next_x][next_y] == 1:
        if horse_child[horse_num]:
            for i in range(len(horse_child[horse_num]) - 1, -1, -1):
                horse_child[i].reverse()
                horse_child[i].append(horse_num)

            start = horse_child[horse_num][-1]
            horse_child[horse_num] = []

            for i in range(1, K + 1):
                if i == start:
                    continue
                if chess_horse[i][0] == next_x and chess_horse[i][1] == next_y:
                    horse_child[i].append(start)
                    if horse_child[start]:
                        horse_child[i] = horse_child[i] + horse_child[start]
        else:
            for i in range(1, K + 1):
                if i == horse_num:
                    continue
                if chess_horse[i][0] == next_x and chess_horse[i][1] == next_y:
                    horse_child[i].append(horse_num)

        chess_horse[horse_num][0], chess_horse[horse_num][1], chess_horse[horse_num][2] = next_x, next_y, now_d


def check_end():
    for i in range(1, K+1):
        if len(horse_child) == K-1:
            return True
    return False


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, K = map(int, input().split())
chess_map = [list(map(int, input().split())) for _ in range(N)]

chess_horse = [[]]
for i in range(1, K + 1):
    x, y, d = map(int, input().split())
    chess_horse.append([x - 1, y - 1, d - 1])

horse_child = [[] for _ in range(K + 1)]

time = 0
while True:
    if time > 1000:
        time = -1
        break
    elif check_end():
        break

    for i in range(1, K + 1):
        move_horse(i)

    time += 1

print(time)
"""

