T = int(input())
for test_case in range(1, T+1):
    table = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    arr = []
    answer = 0
    N = int(input())
    for area in range(1, N+1):
        temp = list(map(int, input().split()))
        arr.append(temp)
    for a in arr:
        for i in range(a[0],a[2]+1):
            for j in range(a[1], a[3]+1):
                if table[i][j] == a[4] or table[i][j] == 0:
                    table[i][j] = a[4]
                else:
                    table[i][j] = 3

    for i in range(10):
        for j in range(10):
            if table[i][j] ==3:
                answer = answer +1
    print("#%d %d" %(test_case, answer))