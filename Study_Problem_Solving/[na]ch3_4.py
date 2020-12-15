N, K = map(int, input().split())
count = 0
while True:

    if N == 1:
        print(count)
        break

    if N % K == 0:
        N = N//K
        count += 1
    else:
        N -= 1
        count += 1

