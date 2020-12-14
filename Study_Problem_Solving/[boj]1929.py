def issosu(k):
    if k == 1:
        return False

    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True

M, N = map(int, input().split())

for i in range(M, N + 1):
    if issosu(i) is True:
        print(i)
    else:
        continue
