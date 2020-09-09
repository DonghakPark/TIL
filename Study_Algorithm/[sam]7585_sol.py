T = int(input())
for test_case in range(1, T+1):
    A,B,N,K = map(int, input().split())
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if((i**A) + (j**B))%K == 0 and i != j:
                count = count+1
    print("#%d %d" %(test_case, count))