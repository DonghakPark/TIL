# import sys
# input = sys.stdin.readline
#
# N = int(input())
#
# series = [0] * 10001
#
# for i in range(N):
#     a = int(input())
#     series[a] = series[a] + 1
#
# for b in range(len(series)):
#     if series[b] != 0:
#         for c in range(series[b]):
#             print(b)
import sys
n = int(sys.stdin.readline())
b = [0] * 10001
for i in range(n):
    b[int(sys.stdin.readline())] += 1
for i in range(10001):
    if b[i] != 0:
        for j in range(b[i]):
            print(i)