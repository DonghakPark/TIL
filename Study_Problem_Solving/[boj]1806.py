"""
부분 합 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""

# N, S = map(int, input().split())
# Sequence = list(map(int, input().split()))
#
# sum_A = [0] * (N+1)
# for i in range(1, N+1):
#     sum_A[i] = sum_A[i-1] + Sequence[i-1]
# start = 0
# end = 1
#
# answer = int(1e9)
#
# while start != N:
#     if sum_A[end] - sum_A[start] >= S:
#         if end - start < answer:
#             answer = end - start
#         start += 1
#
#     else:
#         if end != N:
#             end += 1
#         else:
#             start += 1
# if answer != int(1e9):
#     print(answer)
# else:
#     print(0)

N, S = map(int, input().split())
Sequence = list(map(int, input().split()))
sum_A = [0] * (N+1)
for i in range(1, N+1):
    sum_A[i] = sum_A[i-1] + Sequence[i-1]

answer = int(1e9)
start = 0
end = 1

while start < N:
    if sum_A[end] - sum_A[start] >= S:
        answer = min(answer, end-start)
        start += 1
    else:
        if end != N:
            end += 1
        else:
            start += 1
            
if answer == int(1e9):
    print(0)
else:
    print(answer)