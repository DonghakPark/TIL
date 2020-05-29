T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    Con = list(map(int, input().split()))
    Tru = list(map(int, input().split()))
    Con.sort(reverse=True)
    Tru.sort(reverse=True)
    sum = 0
    for T in range(M):
        if Tru[T] >= Con[0]:
            sum = Con.pop(0) + sum

        elif Tru[T] < Con[0]:
            for i in range(1, len(Con)):
                if Tru[T] >= Con[i]:
                    sum = Con.pop(i)+sum
                    break
        else:
            continue

    print("#{} {}".format(test_case, sum))
