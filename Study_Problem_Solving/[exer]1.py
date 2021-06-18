def solution(n):
    res = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, n-1
    num = 1

    for i in range(n):
        for j in range(i, n):

            if i % 3 == 0:
                x += 1

            elif i % 3 == 1:
                x -= 1
                y -= 1

            elif i % 3 == 2:
                y += 1

            res[x][y] = num
            num += 1

    for i in res:
        for j in i:
            if j != 0:
                answer.append(j)

    return answer

if __name__=="__main__":
    print(solution(4))