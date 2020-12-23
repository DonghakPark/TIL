"""
문자열 뒤집기 문제
"""
S = list(input())
A = []
B = []

k = S.pop(0)

while S:
    temp = S.pop(0)

    if k[-1] == temp:
        k += temp
    elif k[-1] != temp and temp == '1':
        A.append(k)
        k = temp
    elif k[-1] != temp and temp == '0':
        B.append(k)
        k = temp

if k[-1] == '0':
    A.append(k)
else:
    B.append(k)

print(min(len(A),len(B)))

"""
책 풀이
"""
#
# data = input()
# count0 = 0
# count1 = 1
#
# if data[0] == "1":
#     count0 += 1
# else:
#     count1 += 1
#
# for i in range(len(data)-1):
#     if data[i] != data[i+1]:
#         if data[i+1] == "1":
#             count0 += 1
#         else:
#             count1 += 1
# print(min(count1, count0))