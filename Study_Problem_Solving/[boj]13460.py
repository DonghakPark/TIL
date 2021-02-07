"""
구슬 탈출 2 문제
author : donghak park
contact: donghark03@naver.com
TODO : 미해결 --> 다시 풀기
--> 삼성 문제 ( 천천히 해결해 보기 )
"""
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
# 아래, 위, 왼쪽, 오른쪽


def move(direct, board):

    blue_goal = False
    red_goal = False

    # 아래로
    if direct == 0:

        for i in range(N):
            for j in range(M):

                if board[i][j] == "B" or board[i][j] == "R":

                    nx, ny = i + dx[direct], j + dy[direct]

                    if 0 <= nx < N and 0 <= ny < M:

                        if board[nx][ny] == ".":
                            board[nx][ny] = board[i][j]
                            board[i][j] = "."

                        elif board[nx][ny] == "O":

                            if board[i][j] == "R":
                                red_goal = True

                            elif board[i][j] == "B":
                                blue_goal = True

    # 위로
    elif direct == 1:

        for i in range(N-1,-1,-1):
            for j in range(M):

                if board[i][j] == "B" or board[i][j] == "R":

                    nx, ny = i + dx[direct], j + dy[direct]

                    if 0 <= nx < N and 0 <= ny < M:

                        if board[nx][ny] == ".":
                            board[nx][ny] = board[i][j]
                            board[i][j] = "."

                        elif board[nx][ny] == "O":

                            if board[i][j] == "R":
                                red_goal = True

                            elif board[i][j] == "B":
                                blue_goal = True

    # 왼쪽으로
    elif direct == 2:

        for j in range(M-1, -1, -1):
            for i in range(N):

                if board[i][j] == "B" or board[i][j] == "R":

                    nx, ny = i + dx[direct], j + dy[direct]

                    if 0 <= nx < N and 0 <= ny < M:

                        if board[nx][ny] == ".":
                            board[nx][ny] = board[i][j]
                            board[i][j] = "."

                        elif board[nx][ny] == "O":

                            if board[i][j] == "R":
                                red_goal = True

                            elif board[i][j] == "B":
                                blue_goal = True

    # 오른쪽으로
    else:
        for j in range(M):
            for i in range(N):

                if board[i][j] == "B" or board[i][j] == "R":

                    nx, ny = i + dx[direct], j + dy[direct]

                    if 0 <= nx < N and 0 <= ny < M:

                        if board[nx][ny] == ".":
                            board[nx][ny] = board[i][j]
                            board[i][j] = "."

                        elif board[nx][ny] == "O":

                            if board[i][j] == "R":
                                red_goal = True

                            elif board[i][j] == "B":
                                blue_goal = True

    return board, red_goal, blue_goal


def BFS():
    Q = deque()
    for i in range(3,-1,-1):
        Q.append([1, i, board_ori])

    while Q:
        count, dire, arr = Q.popleft()
        print(count, dire, arr)
        arr_new, red_check, blue_check = move(dire, arr)

        if red_check == True and blue_check == False and count <= 10:
            return count

        elif blue_check == False and count <= 10:
            for i in range(4):
                Q.append([count + 1, i,arr_new])

    return -1

N, M = map(int, input().split())
board_ori = [list(input()) for _ in range(N)]
result = BFS()
print(result)
