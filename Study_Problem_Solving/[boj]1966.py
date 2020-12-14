tc = int(input())

for i in range(tc):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))

    K = [False] * len(Q)
    K[M] = True

    count = 0

    while Q:
        if len(Q) == 1:
            count += 1
            print(count)
            break

        temp = Q.pop(0)
        temp2 = K.pop(0)

        if temp < max( Q ):
            Q.append(temp)
            K.append(temp2)
        else:
            count += 1
            if temp2 == True:
                print(count)
                break
            else:
                continue
