tc = int(input())
for i in range(tc):
    H,W,N = map(int, input().split())
    A = N//H+1
    B = N%H
    if B == 0:
        B = H
        A -= 1
    print(B*100+A)