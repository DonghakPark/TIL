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

        temp_al = 'Z'
        temp_x, temp_y = 0, 0

        # 상하 좌우 검사
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < 5 and 0 <= ny < 5:

                if visit[nx][ny] == False and board[nx][ny] > current_Alph:

                    if temp_al >= board[nx][ny]:
                        temp_al = board[nx][ny]
                        temp_x, temp_y = nx, ny

        if temp_x == 0 and temp_y == 0:
            break;

        Q.append((temp_x, temp_y))
        dist[temp_x][temp_y] = dist[x][y] + 1
        visit[temp_x][temp_y] = True

    print(dist)
    return max(dist)


import sys


def DFS(location, count, check):
    global result

    if count > result:
        for e in visit:
            for i in e:
                print(i, end=' ')
            print()
        print()
        result = count

    move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    alpa = board[location[0]][location[1]]

    for move_element in move:
        loc_y = location[0] + move_element[0]
        loc_x = location[1] + move_element[1]
        if loc_y < 5 and loc_y >= 0 and loc_x < 5 and loc_x >= 0:
            if alpa < board[loc_y][loc_x] and not visit[loc_y][loc_x]:
                visit[loc_y][loc_x] = True
                DFS([loc_y, loc_x], count + 1, check)
                visit[loc_y][loc_x] = False
            elif not check and not visit[loc_y][loc_x]:
                visit[loc_y][loc_x] = True
                DFS([loc_y, loc_x], count + 1, True)
                visit[loc_y][loc_x] = False


board = [list(sys.stdin.readline().replace('\n', '')) for i in range(5)]
visit = [[False for i in range(5)] for j in range(5)]
result = 0
visit[0][0] = True
DFS([0, 0], 1, False)
print(result)

if __name__ == "__main__":
    board = [["A", "B", "T", "T", "T"], ["T", "C", "D", "E", "T"], ["T", "T", "T", "F", "T"],
             ["B", "A", "H", "G", "F"], ["C", "D", "E", "F", "G"]]

    print(solution(board))
