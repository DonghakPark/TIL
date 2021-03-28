"""
구슬 탈출 2 문제
author : donghak park
contact: donghark03@naver.com
"""
from collections import deque
import copy

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def move(d, arr, board):
    now_x, now_y = arr

    while True:
        nx, ny = now_x + dx[d], now_y + dy[d]

        if board[nx][ny] == ".":
            now_x, now_y = nx, ny

        elif board[nx][ny] == "O":
            board[arr[0]][arr[1]] = '.'
            return now_x, now_y, True, board

        else:
            board[now_x][now_y] = board[arr[0]][arr[1]]
            if now_x != arr[0] or now_y != arr[1]:
                board[arr[0]][arr[1]] = '.'
            return now_x, now_y, False, board


def solution():
    global answer

    Q = deque()
    for i in range(4):
        # direct, time
        new_board = copy.deepcopy(board)
        Q.append([i, 1, red_ball, blue_ball, new_board])

    while Q:

        direct, time, red_ball_now, blue_ball_now, now_board = Q.popleft()

        if time >= 11:
            return

        if direct == 0:
            if red_ball_now[1] > blue_ball_now[1]:
                red_nx, red_ny, red_flag, new_board = move(direct, red_ball_now, now_board)
                blue_nx, blue_ny, blue_flag, new_board = move(direct, blue_ball_now, now_board)
            else:
                blue_nx, blue_ny, blue_flag, new_board = move(direct, blue_ball_now, now_board)
                red_nx, red_ny, red_flag, new_board = move(direct, red_ball_now, now_board)
        elif direct == 1:
            if red_ball_now[1] < blue_ball_now[1]:
                red_nx, red_ny, red_flag, new_board = move(direct, red_ball_now, now_board)
                blue_nx, blue_ny, blue_flag, new_board = move(direct, blue_ball_now, now_board)
            else:
                blue_nx, blue_ny, blue_flag, new_board = move(direct, blue_ball_now, now_board)
                red_nx, red_ny, red_flag, new_board = move(direct, red_ball_now, now_board)
        elif direct == 2:
            if red_ball_now[0] < blue_ball_now[0]:
                red_nx, red_ny, red_flag, new_board = move(direct, red_ball_now, now_board)
                blue_nx, blue_ny, blue_flag, new_board = move(direct, blue_ball_now, now_board)
            else:
                blue_nx, blue_ny, blue_flag, new_board = move(direct, blue_ball_now, now_board)
                red_nx, red_ny, red_flag, new_board = move(direct, red_ball_now, now_board)
        else:
            if red_ball_now[0] > blue_ball_now[0]:
                red_nx, red_ny, red_flag, new_board = move(direct, red_ball_now, now_board)
                blue_nx, blue_ny, blue_flag, new_board = move(direct, blue_ball_now, now_board)
            else:
                blue_nx, blue_ny, blue_flag, new_board = move(direct, blue_ball_now, now_board)
                red_nx, red_ny, red_flag, new_board = move(direct, red_ball_now, now_board)

        if (blue_flag is False) and (red_flag is False):
            if [red_nx, red_ny] != red_ball_now or [blue_nx, blue_ny] != blue_ball_now:
                for i in range(4):
                    next_board = copy.deepcopy(new_board)
                    Q.append([i, time + 1, [red_nx, red_ny], [blue_nx, blue_ny], next_board])

        elif (red_flag is True) and (blue_flag is False):
            answer = time
            return


N, M = map(int, input().split())
board = []

red_ball = [0, 0]
blue_ball = [0, 0]

for col in range(N):
    S = list(input())

    for i in range(len(S)):
        if S[i] == "R":
            red_ball = [col, i]
        elif S[i] == "B":
            blue_ball = [col, i]
    board.append(S)

answer = -1
solution()

print(answer)
