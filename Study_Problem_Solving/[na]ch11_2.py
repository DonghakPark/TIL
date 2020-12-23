"""
곱하기 혹은 더하기
"""
S = list(map(int,input()))

answer = S.pop(0)

while S:
    temp = S.pop(0)

    if answer == 0:
        answer += temp
    elif temp == 0 or temp == 1:
        answer += temp
    else:
        answer *= temp
print(answer)

"""
책 풀이
"""

# data = input()
#
# result = int(data[0])
#
# for i in range(1, len(data)):
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
# print(result)