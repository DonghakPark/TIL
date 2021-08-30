from collections import deque

def solution(board):
    answer = 0
    #     0  1  2  3
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    N = len(board)
    cost_map = [[1e9]*N for _ in range(N)]
    cost_map[0][0] = 0
    q = deque()
    answer_candidate = []

    if board[0][1] == 0:
        q.append([100, 0, 1, 0])
        cost_map[0][1] = 100
    if board[1][0] == 0:
        q.append([100, 1, 0, 1])
        cost_map[1][0] = 100

    while q:
        now_cost, now_x, now_y, last_dir = q.popleft()

        if now_x == N-1 and now_y == N-1:
            answer_candidate.append(now_cost)
            continue

        for i in range(4):
            nx, ny = now_x + dx[i], now_y + dy[i]
            if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                if board[nx][ny] == 0:

                    if last_dir == i % 2 and cost_map[nx][ny] >= now_cost + 100:
                        q.append([now_cost + 100, nx, ny, i % 2])
                        cost_map[nx][ny] = now_cost + 100
                    elif last_dir != i % 2 and cost_map[nx][ny] >= now_cost + 600:
                        q.append([now_cost + 600, nx, ny, i % 2])
                        cost_map[nx][ny] = now_cost + 600

    # print(answer_candidate)
    answer = min(answer_candidate)
    return answer


if __name__ == "__main__":
    print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 900)
    print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]), 3800)
    print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]), 2100)
    print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]),3200)