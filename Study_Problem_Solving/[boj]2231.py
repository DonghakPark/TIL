N = int(input())

for n in range(1, N+1):
    k = list(map(int, str(n)))
    temp = n + sum(k)
    if temp == N:
        print(n)
        break
    if n == N:
        print(0)
        break