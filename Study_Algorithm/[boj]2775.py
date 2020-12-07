tc = int(input())
for i in range(tc):
    k = int(input())
    n = int(input())
    base = [j for j in range(1, n+1)]

    for l in range(k):
        for m in range(1,n):
            base[m] += base[m-1]
    print(base[n-1])

