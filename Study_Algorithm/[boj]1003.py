# def fibonacci(n):
#     global count_0
#     global count_1
#
#     if n == 0:
#         count_0 += 1
#         return False
#     elif n == 1:
#         count_1 += 1
#         return True
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# tc = int(input())
#
# for i in range(tc):
#     count_0 = 0
#     count_1 = 0
#     N = int(input())
#     fibonacci(N)
#     print("{} {}".format(count_0, count_1))

a = int(input())

zero = [1, 0, 1]
one = [0, 1, 1]


def cal(num):
    length = len(zero)
    if length <= num:
        for i in range(length, num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print("%d %d" % (zero[num], one[num]))


for i in range(a):
    k = int(input())
    cal(k)
