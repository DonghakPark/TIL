def GCD(p,q):
    if p <q:
        return GCD(q, p)
    elif q == 0:
        return p
    else:
        return GCD(q, p%q)

T = int(input())

for test_case in range(1,T+1):
    R,N,K = map(int, input().split())
    Arr = []
    for robot in range(1, N+1):
        x,y = map(int, input().split())
        Arr.append([x,y])


