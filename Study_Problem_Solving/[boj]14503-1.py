
# 0 : 북 / 1 : 동 / 2 : 남 / 3 : 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def solution(graph, r, c, d):
    answer = 0
    count = 0

    while True:
        # 현재위치 청소
        if graph[r][c] == 0:
            graph[r][c] = 2
            answer += 1

        if d == 0:
            d = 3
        else:
            d -= 1

        count += 1
        nr = r + dr[d]
        nc = c + dc[d]

        if graph[nr][nc] == 0:
            count = 0
            r, c = nr, nc
            continue

        if count == 4:
            nr = r - dr[d]
            nc = c - dc[d]
            if graph[nr][nc] == 0 or graph[nr][nc] == 2:
                count = 0
                r, c = nr, nc
            elif graph[nr][nc] == 1:
                break

    return answer

if __name__ == "__main__":
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    print(solution(graph, r, c, d))