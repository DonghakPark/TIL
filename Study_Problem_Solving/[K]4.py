from collections import defaultdict


def calc_score(board, a_board):
    global candidate_answer

    a_score = 0
    b_score = 0

    candidate_board = [0 for _ in range(11)]

    for i in range(11):
        if board[i]:
            b_score += 10 - i
            candidate_board[i] += a_board[i] + 1
        elif board[i] == False and a_board[i] != 0:
            a_score += 10 - i

    diff = b_score - a_score

    if diff > 0 and candidate_board not in candidate_answer[diff]:
        candidate_answer[diff].append(candidate_board)

    return


def calc_score2(board, a_board, left):
    global candidate_answer

    a_score = 0
    b_score = 0

    candidate_board = [0 for _ in range(11)]

    for i in range(11):
        if board[i]:
            b_score += 10 - i
            candidate_board[i] += a_board[i] + 1
        elif board[i] == False and a_board[i] != 0:
            a_score += 10 - i

    diff = b_score - a_score

    for i in range(10, -1, -1):
        if board[i] is False:
            while left > 0 and a_board[i] > candidate_board[i]:
                candidate_board[i] += 1
                left -= 1

    if diff > 0 and candidate_board not in candidate_answer[diff]:
        candidate_answer[diff].append(candidate_board)

    return


def make_board(board, n, a_board, start, original_n):
    if n == 0:
        calc_score(board, a_board)
        return

    for i in range(start, 11):
        if n - (a_board[i] + 1) >= 0:
            board[i] = True
            make_board(board, n - (a_board[i] + 1), a_board, i + 1, original_n)
            board[i] = False

    if n > 0:
        calc_score2(board, a_board, n)


def solution(n, info):
    global candidate_answer
    answer = []

    candidate_answer = defaultdict(list)
    win_board = [False for _ in range(11)]

    make_board(win_board, n, info, 0, n)

    if len(candidate_answer.keys()) == 0:
        return [-1]

    else:
        max_key = max(candidate_answer.keys())
        candidate = candidate_answer[max_key]
        if len(candidate) == 1:
            return candidate[0]
        else:
            temp = []
            for element in candidate:
                temp.append(element[::-1])
                temp.sort(reverse=True)
            return temp[0][::-1]


if __name__ == "__main__":
    print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]), [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0])
    print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), [-1])
    print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]), [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0])
    print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]), [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2])
