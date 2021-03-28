import math
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    an = -1
    answer = int(round(pow(n, 1.0/3.0), 2))
    if pow(answer, 3) == n:
        print("#{} {}".format(test_case, answer))
    else:
        print("#{} {}".format(test_case, an))
