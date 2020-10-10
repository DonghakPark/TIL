TC = int(input())

for test_case in range(1,TC+1):
    N, M = map(int, input().split())

    bin_M = bin(M)[2:]

    if len(bin_M) < N or M == 0:
        print("#{} {}".format(test_case, "OFF"))
        continue

    count = 0

    for i in range(1,N+1):

        if bin_M[-i] == '1':
            count += 1
        else:
            continue

    if count == N:
        print("#{} {}".format(test_case, "ON"))
    else:
        print("#{} {}".format(test_case, "OFF"))
