T = int(input())
for test_case in range(1, T+1):
    N, A, B = map(int, input().split())

    Min = A+B-N
    if Min < 0:
        Min = 0
    Max = 0
    if A > B:
        Max = B
    else:
        Max = A

    print("#{} {} {}".format(test_case, Max, Min))
