def solution(land):
    answer = 0
    dp_table = [[0] * 4 for _ in range(len(land))]
    dp_table[0] = land[0]

    for i in range(1, len(land)):
        for j in range(4):
            for k in range(4):
                if j == k:
                    continue
                else:
                    dp_table[i][j] = max(dp_table[i][j], dp_table[i - 1][k] + land[i][j])
    answer = max(dp_table[len(land) - 1])
    return answer