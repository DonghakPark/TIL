# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초 연산이다.
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    min, max = 99999999,0
    for i in range(0, N-M+1):
        temp = sum(arr[i:i+M])
        if temp < min:
            min = temp
        if temp > max:
            max = temp
    print("#%d %d" %(test_case, max-min))