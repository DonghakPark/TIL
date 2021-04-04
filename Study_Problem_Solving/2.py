def solution(rows, columns, queries):
    answer = []
    arr = [[0] * columns for _ in range(rows)]

    num_order = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = num_order
            num_order += 1

    for query in queries:
        x1, y1, x2, y2 = query
        x1, y1, x2, y2 = [x1-1, y1-1, x2-1, y2-1]
        temp_arr = []

        # 윗줄
        for i in range(y1, y2+1):
            temp_arr.append(arr[x1][i])
        # 오른쪽
        for i in range(x1+1, x2+1):
            temp_arr.append(arr[i][y2])
        # 밑
        for i in range(y2-1, y1-1, -1):
            temp_arr.append(arr[x2][i])
        # 왼쪽
        for i in range(x2-1, x1, -1):
            temp_arr.append(arr[i][y1])

        change = temp_arr.pop()
        temp_arr.insert(0, change)
        answer.append(min(temp_arr))

        # 윗줄
        for i in range(y1, y2 + 1):
            arr[x1][i] = temp_arr.pop(0)
        # 오른쪽
        for i in range(x1 + 1, x2 + 1):
            arr[i][y2] = temp_arr.pop(0)
        # 밑
        for i in range(y2 - 1, y1 - 1, -1):
            arr[x2][i] = temp_arr.pop(0)
        # 왼쪽
        for i in range(x2 - 1, x1, -1):
            arr[i][y1] = temp_arr.pop(0)

    return answer

if __name__=="__main__":
     print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]), 	[8, 10, 25])
     print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]), [1,1,5,3])
     print(solution(100, 97, [[1, 1, 100, 97]]), [1])