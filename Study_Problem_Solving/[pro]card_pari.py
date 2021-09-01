from itertools import permutations
from collections import deque, defaultdict
from copy import deepcopy

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def ctrl_move(x, y, d):
    global board_copy
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            return x, y
        else:
            if board_copy[nx][ny] != 0:
                return nx, ny
            x, y = nx, ny


def find_route(start, end):
    global board_copy

    sx, sy = start
    ex, ey = end

    if sx == ex and sy == ey:
        return 1

    q = deque()
    q.append([sx, sy])

    table = [[0] * 4 for _ in range(4)]
    visited = [[True] * 4 for _ in range(4)]
    visited[sx][sy] = False

    while q:
        x, y = q.popleft()

        for i in range(4):

            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4 and visited[nx][ny]:
                table[nx][ny] = table[x][y] + 1
                visited[nx][ny] = False
                if nx == ex and ny == ey:
                    return table[nx][ny] + 1
                q.append([nx, ny])

            nx, ny = ctrl_move(x, y, i)
            if visited[nx][ny]:
                table[nx][ny] = table[x][y] + 1
                visited[nx][ny] = False
                if nx == ex and ny == ey:
                    return table[nx][ny] + 1
                q.append([nx, ny])


def delete_card(card):
    global board_copy, card_pos

    for x, y in card_pos[card]:
        board_copy[x][y] = 0


def store_card(card):
    global board_copy, card_pos

    for x, y in card_pos[card]:
        board_copy[x][y] = card

def search(x,y, order, card_number, count, move):
    global answer, orders, card_pos, board_copy

    if count == card_number:
        answer = min(answer, move)
        return

    card = orders[order][count]

    first = card_pos[card][0]
    second = card_pos[card][1]

    d1 = find_route([x,y], [first[0], first[1]])
    d2 = find_route([first[0], first[1]], [second[0], second[1]])

    delete_card(card)
    search(second[0], second[1], order, card_number, count+1, move+d1+d2)
    store_card(card)

    d1 = find_route([x,y], [second[0],second[1]])
    d2 = find_route([second[0],second[1]], [first[0], first[1]])

    delete_card(card)
    search(first[0], first[1], order, card_number, count + 1, move + d1 + d2)
    store_card(card)

def solution(board, r, c):
    global answer, orders, card_pos, board_copy

    answer = int(1e9)
    board_copy = deepcopy(board)
    card_pos = defaultdict(list)

    for i in range(4):
        for j in range(4):
            num = board[i][j]
            if num != 0:
                card_pos[num].append([i, j])

    order = [k for k, v in card_pos.items()]
    orders = list(permutations(order, len(order)))

    for i in range(len(orders)):
        search(r,c,i,len(card_pos.keys()), 0, 0)

    return answer


if __name__ == "__main__":
    print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0), 14)
    print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1), 16)
