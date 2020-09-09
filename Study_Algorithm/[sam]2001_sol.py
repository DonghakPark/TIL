T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    Matrix = []

    for n in range(0,N):
        temp = list(map(int, input().split()))
        Matrix.append(temp)
    sum = 0
    max = 0
    for i in range(0,N-M+1):
        for j in range(0, N-M+1):

            for k in range(i, i+M):
                for z in range(j, j+M):
                    sum += Matrix[k][z]

            if sum >= max:
                max = sum
            sum = 0
    print("#{} {}".format(test_case, max))