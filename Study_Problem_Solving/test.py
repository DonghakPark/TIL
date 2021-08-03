def solution(rows, columns, swipes):
    answer = []
    board = [[0] * columns for _ in range(rows)]

    init_num = 1
    for i in range(0, rows):
        for j in range(0, columns):
            board[i][j] = init_num
            init_num += 1

    while swipes:

        d, r1, c1, r2, c2 = swipes.pop(0)

        temp_arr = [ [0] * (c2- c1 + 1) for _ in range(r2 - r1 + 1)]

        temp_answer = 0

        for row in range(r1 - 1 , r2):
            for col in range(c1 - 1, c2):

                if d == 1:
                    temp_arr[(row + 1 - (r1-1))%len(temp_arr)][col - (c1-1)] = board[row][col]

                    if row == r2 - 1:
                        temp_answer += board[row][col]

                elif d == 2:
                    temp_arr[(row - 1 - (r1-1))%len(temp_arr)][col - (c1-1)] = board[row][col]

                    if row == r1 - 1 :
                        temp_answer += board[row][col]

                elif d == 3:
                    temp_arr[row - (r1-1)][(col + 1 - (c1-1)) % len(temp_arr[0])] = board[row][col]

                    if col == c2 - 1:
                        temp_answer += board[row][col]

                elif d == 4:
                    temp_arr[row - (r1-1)][(col - 1 - (c1-1)) % len(temp_arr[0])] = board[row][col]

                    if col == c1 - 1:
                        temp_answer += board[row][col]

        for i in range(0, len(temp_arr)):
            for j in range(0, len(temp_arr[0])):
                board[i + (r1 -1)][j+ (c1-1)] = temp_arr[i][j]

        answer.append(temp_answer)

    return answer
