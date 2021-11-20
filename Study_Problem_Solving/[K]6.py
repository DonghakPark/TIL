from copy import deepcopy


def repair(left, right, i, skill):
    global gl_board

    while right - left > 0:
        gl_board[i][left] += skill
        left += 1
        if left + 1 == right:
            continue
        gl_board[i][right] += skill
        right -= 1


def attack(left, right, i, skill):
    global gl_board

    while right - left > 0:
        gl_board[i][left] -= skill
        left += 1
        if left + 1 == right:
            continue
        gl_board[i][right] -= skill
        right -= 1


def solution(board, skill):
    global gl_board
    gl_board = deepcopy(board)
    answer = 0

    for element in skill:
        for i in range(element[1], element[3] + 1):
            left, right = element[2], element[4]

            if left == right:
                if element[0] == 1:
                    gl_board[i][left] -= element[-1]
                else:
                    gl_board[i][left] += element[-1]
            elif element[0] == 1:
                attack(left, right, i, element[-1])
            else:
                repair(left, right, i, element[-1])

    for i in range(len(board)):
        for j in range(len(board[0])):
            if gl_board[i][j] > 0:
                answer += 1
    return answer
