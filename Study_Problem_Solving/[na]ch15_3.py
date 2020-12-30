"""
공유기 설치 문제
author : donghak park
contact : donghark03@naver.com
TODO : 다시 풀어보기 -> 책도 틀리게 나옴
"""

# N, C = list(map(int, input().split(' ')))
#
# home = []
# for _ in range(N):
#     home.append(int(input()))
# home.sort()
#
# start = home[1] - home[0]
# end = home[-1] - home[0]
# answer = 0
#
# while (start <= end):
#     mid = (start + end) // 2
#     value = home[0]
#     count = 1
#
#     for i in range(1, N):
#         if home[i] >= value + mid:
#             value = home[i]
#             count += 1
#     if count >= C:
#         start = mid + 1
#         answer = mid
#     else:
#         end = mid - 1
#
# print(answer)

def solve(lst, target, low, high):
    if low > high:
        return (low + high) // 2
    mid, count = (low + high) // 2, 1
    tmp = lst[0]
    for i in range(1, len(lst)):
        if lst[i] - tmp >= mid:
            count += 1
            tmp = lst[i]
    if count >= target:
        return solve(lst, target, mid+1, high)
    if count < target:
        return solve(lst, target, low, mid-1)

N, C = map(int, input().split())
loc = []
for _ in range(N):
    loc.append(int(input()))
loc.sort()
result = solve(loc, C, 1, loc[-1]-loc[0])
print(result)