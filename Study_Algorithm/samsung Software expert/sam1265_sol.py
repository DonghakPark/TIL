
T = int(input())
for test_case in range(1, T+1):
    N, P = map(int, input().split())
    A = N//P
    B = N%P
    ans = A**(P-B) * (A+1)**B
    print("#%d %d" %(test_case, ans))
