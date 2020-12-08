import sys
from math import sqrt
input = sys.stdin.readline
output = sys.stdout.write

# 제곱근 분할법
def solve():
  n, _, _ = map(int, input().split())
  sqrt_n = int(sqrt(n))
  bucket = [0 for _ in range(sqrt_n + 1)]
  cnt = [0 for _ in range(n + 1)]
  temp = list(map(int, input().split()))
  for v in temp:
      bucket[v // sqrt_n] += 1
      cnt[v] += 1
  temp = list(map(int, input().split()))
  for a in temp:
      for j in range(a // sqrt_n, n // sqrt_n + 1):
          flag = False
          if bucket[j]:
              for b in range(max(a+1, j * sqrt_n), (j+1) * sqrt_n + 1):
                  if cnt[b] > 0:
                      output(str(b) + '\n')
                      cnt[b] -= 1
                      bucket[j] -= 1
                      flag = True
                      break
          if flag:
              break

if __name__ == '__main__':
  solve()

# import sys
# import math
#
# N, M, K = map(int, sys.stdin.readline().split())
# M_arr = list(map(int, sys.stdin.readline().split()))
# K_arr = list(map(int, sys.stdin.readline().split()))
#
# def upperBound(start, end, key):
#     while ( end - start > 0):
#         mid = (start + end )//2
#         if M_arr[mid] <= key:
#             start = mid + 1
#         else:
#             end = mid
#     return end
#
# M_arr.sort()
#
# for element in K_arr:
#     result = (upperBound(0, len(M_arr), element))
#     print(M_arr.pop(result))
