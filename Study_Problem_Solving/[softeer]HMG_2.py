import sys, math
from collections import deque, defaultdict


def best_seat(x, y):
    candidate = []

    for i in range(N):
        for j in range(M):
            if lunch_map[i][j] > 0:
                candidate.append([math.sqrt((x - i) ** 2 + (y - j) ** 2), x, y])
    candidate.sort(key=lambda x: (x[0], x[1], x[2]))
    if candidate:
        return candidate[0][0], candidate[0][1], candidate[0][2]
    else:
        return -1, -1, -1


N, M, Q = map(int, input().split())
commands = []

for _ in range(Q):
    in_out, s_id = map(str, input().split())
    commands.append([in_out, int(s_id)])

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

lunch_map = [[0] * M for _ in range(N)]
id_seat = defaultdict(list)
commands = deque(commands)
in_lunch = deque()
already_lunch = deque()

while commands:
    now_in_out, now_id = commands.popleft()
    # 식사하러 왔을 때
    if now_in_out == "In":

        if now_id in in_lunch:
            print("{} already seated.".format(now_id))

        elif now_id in already_lunch:
            print("{} already ate lunch.".format(now_id))

        else:

            if len(in_lunch) == 0:
                in_lunch.append(now_id)
                lunch_map[0][0] = now_id
                id_seat[now_id].extend([0, 0])
                if M >= 2:
                    lunch_map[0][1] = -1
                if N >= 2:
                    lunch_map[1][0] = -1
                print("{} gets the seat ({}, {}).".format(now_id, 1, 1))
            else:
                candidate_seat = []
                for i in range(N):
                    for j in range(M):
                        if lunch_map[i][j] == 0:
                            D, nx, ny = best_seat(i, j)
                            if [D, nx, ny] != [-1, -1, -1]:
                                candidate_seat.append([D, nx, ny])

                if len(candidate_seat) == 0:
                    print("There are no more seats.")
                else:
                    candidate_seat.sort(key=lambda x: (x[0], x[1], x[2]))
                    next_x, next_y = candidate_seat[0][1], candidate_seat[0][2]

                    for k in range(4):
                        no_x, no_y = next_x + dx[k], next_y + dy[k]

                        if 0 <= no_x < N and 0 <= no_y < M:
                            lunch_map[no_x][no_y] -= 1

                    lunch_map[next_x][next_y] = now_id
                    print("{} gets the seat ({}, {}).".format(now_id, next_x + 1, next_y + 1))
                    in_lunch.append(now_id)
                    id_seat[now_id].extend([next_x, next_y])

    # 밥먹고 나갈 때
    elif now_in_out == "Out":

        if now_id not in in_lunch and now_id not in already_lunch:
            print("{} didn't eat lunch.".format(now_id))

        elif now_id in already_lunch:
            print("{} already left seat.".format(now_id))

        else:
            print("{} leaves from the seat ({}, {}).".format(now_id, id_seat[now_id][0] + 1, id_seat[now_id][1] + 1))

            in_lunch.remove(now_id)
            already_lunch.append(now_id)

            now_x, now_y = id_seat[now_id]

            lunch_map[now_x][now_y] = 0

            for i in range(4):
                nx, ny = now_x + dx[i], now_y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    lunch_map[nx][ny] += 1

