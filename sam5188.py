def DFS(row, col):
    down = right = N ** 4  # 범위 밖 가상의 값

    if row == col >= N - 1:  # 마지막 지점 도착
        return my_map[row][col]
    else:
        if row < N - 1:  # 아래쪽 끝이 아니면
            down = DFS(row + 1, col)
        if col < N - 1:  # 오른쪽 끝이 아니면
            right = DFS(row, col + 1)

    if down < right:  # 작은 값 취함
        return down + my_map[row][col]
    else:
        return right + my_map[row][col]


T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    my_map = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(test_case, DFS(0, 0)))