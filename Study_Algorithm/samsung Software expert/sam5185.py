T = int(input())
for test_case in range(1, T+1):
    N, K = map(str, input().split())
    N = int(N)
    K = int(K,16)
    k = format(K, 'b')
    print("#%d %s" %(test_case, k))

