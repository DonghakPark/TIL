def solution(board):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    Q = []

    visit = [[False] * 5 for i in range(5)]
    dist = [[0] * 5 for i in range(5)]

    Q.append((0, 0))
    current_Alph = board[0][0]
    visit[0][0] = True
    dist[0][0] = 1
    revisit = False

    while Q:
        x, y = Q.pop(0)
        current_Alph = board[x][y]
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < 5 and 0 <= ny < 5:
                if visit[nx][ny] == False and board[nx][ny] > current_Alph:
                    Q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
                    visit[nx][ny] = True

    answer = 0

    for element in dist:
        for j in element:
            if j > answer:
                answer = j

    return answer


if __name__ == "__main__":
    board = [["A", "B", "T", "T", "T"], ["T", "C", "D", "E", "T"], ["T", "T", "T", "F", "T"],
             ["B", "A", "H", "G", "F"], ["C", "D", "E", "F", "G"]]

    print(solution(board))