"""
이차원 배열과 연산
Author : DongHak Park
"""

r, c, k = map(int, input().split())

arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))

time = 0
while True:

    row_len = len(arr)
    col_len = len(arr[0])

    if 0 <= r - 1 < row_len and 0 <= c - 1 < col_len and arr[r - 1][c - 1] == k:
        print(time)
        break
    if time > 100:
        print(-1)
        break

    if row_len >= col_len:
        # 정렬 후 삽입까지
        new_arr = [[] for _ in range(row_len)]
        max_len = 0
        for i in range(len(arr)):
            set_row = set(arr[i])
            if 0 in set_row:
                set_row.remove(0)

            pair_row = []
            for element in set_row:
                pair_row.append([element, arr[i].count(element)])
            pair_row.sort(key=lambda x: (x[1], x[0]))

            for element in pair_row:
                for element2 in element:
                    new_arr[i].append(element2)
            max_len = max(max_len, len(new_arr[i]))

        # 길이 맞춰주기
        for i in range(len(new_arr)):
            extend_arr = [0] * (max_len - len(new_arr[i]))
            new_arr[i].extend(extend_arr)
        arr = new_arr
    else:
        new_arr = [[0] * col_len for _ in range(row_len * 3)]
        max_len = 0

        for i in range(len(arr[0])):
            temp_arr = []
            for j in range(len(arr)):
                temp_arr.append(arr[j][i])
            set_col = set(temp_arr)
            if 0 in set_col:
                set_col.remove(0)
            pair_col = []
            for element in set_col:
                pair_col.append([element, temp_arr.count(element)])
            pair_col.sort(key=lambda x: (x[1], x[0]))

            local_len = len(pair_col) * 2
            max_len = max(max_len, local_len)
            index = 0

            for element in pair_col:
                for element2 in element:
                    new_arr[index][i] = element2
                    index += 1

        now_len = len(new_arr)
        for _ in range(now_len - max_len):
            new_arr.pop()

        arr = new_arr

    time += 1

    # row가 100개 초과
    now_row_len = len(arr)
    now_col_len = len(arr[0])
    for _ in range(now_row_len - 100):
        arr.pop()

    for i in range(len(arr)):
        for _ in range(now_col_len - 100):
            arr[i].pop()
