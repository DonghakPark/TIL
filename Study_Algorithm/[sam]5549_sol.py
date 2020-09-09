T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    if N%2 ==0:
        print("#{} {}".format(test_case, "Even"))
    else:
        print("#{} {}".format(test_case, "Odd"))